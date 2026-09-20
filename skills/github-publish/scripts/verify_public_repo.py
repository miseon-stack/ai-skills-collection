#!/usr/bin/env python3
"""Compare a local file tree with a public GitHub repository tree."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


DEFAULT_EXCLUDES = (
    ".git",
    ".git/**",
    ".DS_Store",
    "**/.DS_Store",
    "__pycache__",
    "**/__pycache__/**",
    ".pytest_cache",
    "**/.pytest_cache/**",
)

REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


class VerificationError(RuntimeError):
    pass


def normalize_relative(value: str, label: str) -> str:
    value = value.replace("\\", "/").strip("/")
    if not value:
        return ""
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts:
        raise VerificationError(f"{label} must be a safe repository-relative path")
    return path.as_posix()


def matches_any(path: str, patterns: Iterable[str]) -> bool:
    return any(fnmatch.fnmatchcase(path, pattern) for pattern in patterns)


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def local_manifest(root: Path, patterns: tuple[str, ...]) -> dict[str, str]:
    if not root.is_dir():
        raise VerificationError(f"local directory does not exist: {root}")

    manifest: dict[str, str] = {}
    for current, dirnames, filenames in os.walk(root, followlinks=False):
        current_path = Path(current)

        kept_dirs: list[str] = []
        for dirname in dirnames:
            directory = current_path / dirname
            rel = directory.relative_to(root).as_posix()
            if directory.is_symlink():
                raise VerificationError(f"symlink is not supported by web publishing: {rel}")
            if not matches_any(rel, patterns) and not matches_any(f"{rel}/x", patterns):
                kept_dirs.append(dirname)
        dirnames[:] = kept_dirs

        for filename in filenames:
            path = current_path / filename
            rel = path.relative_to(root).as_posix()
            if matches_any(rel, patterns):
                continue
            if path.is_symlink():
                raise VerificationError(f"symlink is not supported by web publishing: {rel}")
            manifest[rel] = git_blob_sha(path.read_bytes())

    return manifest


def github_json(url: str) -> dict:
    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "github-publish-skill/1.0",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            return json.load(response)
    except HTTPError as exc:
        if exc.code == 404:
            raise VerificationError(
                "GitHub returned 404. Check the repository name and branch; "
                "private repositories cannot be verified without authentication."
            ) from exc
        if exc.code == 403:
            raise VerificationError(
                "GitHub returned 403. The unauthenticated API rate limit may be exhausted."
            ) from exc
        raise VerificationError(f"GitHub API returned HTTP {exc.code}") from exc
    except (URLError, TimeoutError) as exc:
        raise VerificationError(f"could not reach GitHub API: {exc}") from exc


def remote_manifest(
    repo: str, branch: str | None, remote_subdir: str, patterns: tuple[str, ...]
) -> tuple[dict[str, str], dict, str]:
    metadata = github_json(f"https://api.github.com/repos/{repo}")
    if metadata.get("private"):
        raise VerificationError("this verifier supports public repositories only")

    resolved_branch = branch or metadata.get("default_branch")
    if not resolved_branch:
        raise VerificationError("could not determine the target branch")

    tree_url = (
        f"https://api.github.com/repos/{repo}/git/trees/"
        f"{quote(resolved_branch, safe='')}?recursive=1"
    )
    tree = github_json(tree_url)
    if tree.get("truncated"):
        raise VerificationError("GitHub truncated the recursive tree; use a Git-aware verifier")

    prefix = f"{remote_subdir}/" if remote_subdir else ""
    manifest: dict[str, str] = {}
    for item in tree.get("tree", []):
        if item.get("type") != "blob":
            continue
        path = item.get("path", "")
        if prefix:
            if not path.startswith(prefix):
                continue
            path = path[len(prefix) :]
        if not path or matches_any(path, patterns):
            continue
        manifest[path] = item.get("sha", "")

    return manifest, metadata, resolved_branch


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare local paths and Git blob hashes with a public GitHub repository."
    )
    parser.add_argument("local_dir", type=Path, help="local directory to compare")
    parser.add_argument("repo", help="GitHub repository in OWNER/REPO form")
    parser.add_argument("--branch", help="branch or ref; defaults to the repository default branch")
    parser.add_argument(
        "--remote-subdir",
        default="",
        help="repository subdirectory corresponding to local_dir",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        metavar="GLOB",
        help="additional local and remote relative-path glob to ignore; repeatable",
    )
    parser.add_argument(
        "--no-default-excludes",
        action="store_true",
        help="include files normally excluded by the verifier",
    )
    parser.add_argument("--json", action="store_true", help="print machine-readable output")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not REPO_RE.fullmatch(args.repo):
        print("error: repo must use OWNER/REPO form", file=sys.stderr)
        return 2

    try:
        remote_subdir = normalize_relative(args.remote_subdir, "remote subdirectory")
        base_patterns = () if args.no_default_excludes else DEFAULT_EXCLUDES
        patterns = tuple(base_patterns) + tuple(args.exclude)
        local = local_manifest(args.local_dir.resolve(), patterns)
        remote, metadata, branch = remote_manifest(
            args.repo, args.branch, remote_subdir, patterns
        )
    except (OSError, VerificationError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    local_paths = set(local)
    remote_paths = set(remote)
    missing = sorted(local_paths - remote_paths)
    extra = sorted(remote_paths - local_paths)
    mismatched = sorted(
        path for path in local_paths & remote_paths if local[path] != remote[path]
    )
    ok = not missing and not extra and not mismatched

    result = {
        "ok": ok,
        "repository": args.repo,
        "url": metadata.get("html_url"),
        "visibility": metadata.get("visibility"),
        "default_branch": metadata.get("default_branch"),
        "checked_branch": branch,
        "remote_subdir": remote_subdir,
        "local_file_count": len(local),
        "remote_file_count": len(remote),
        "missing": missing,
        "extra": extra,
        "mismatched": mismatched,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"repository: {args.repo}")
        print(f"url: {result['url']}")
        print(f"visibility: {result['visibility']}")
        print(f"default branch: {result['default_branch']}")
        print(f"checked branch: {branch}")
        print(f"remote scope: {remote_subdir or '/'}")
        print(f"local files: {len(local)}")
        print(f"remote files: {len(remote)}")
        print(f"missing: {len(missing)}")
        for path in missing:
            print(f"  - {path}")
        print(f"extra: {len(extra)}")
        for path in extra:
            print(f"  + {path}")
        print(f"mismatched: {len(mismatched)}")
        for path in mismatched:
            print(f"  ! {path}")
        print("result: MATCH" if ok else "result: MISMATCH")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
