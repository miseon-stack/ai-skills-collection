---
name: github-publish
description: Publish or update local Codex skills and other small file trees in a GitHub repository through the user's already-authenticated GitHub web session when CLI, API, device-flow, Google social-login, or email verification is unavailable. Use when the user explicitly asks to upload, open-source, publish, or update local files via a GitHub account that is already signed in in Chrome or the in-app browser. Prepare a safe manifest, preserve licenses and attribution, create or edit files from the repository root, recover accidental nested paths, and verify remote paths plus Git blob hashes. Never use this skill to bypass login, email verification, 2FA, sudo mode, repository permissions, or to inspect or export passwords, cookies, tokens, local storage, profiles, or session data.
---

# GitHub Web Publisher

Publish through a GitHub session the user already controls. Treat the web session as an authorized UI surface, not as a source of credentials and not as permission to defeat a reauthentication boundary.

## Safety invariants

- Require an explicit request to publish or update the identified files and repository.
- Require an explicit request before creating a public repository. Otherwise preserve the existing visibility or ask.
- Never inspect, copy, export, log, or request browser passwords, cookies, tokens, profiles, local storage, verification codes, or recovery data.
- Never bypass GitHub login, sudo mode, email verification, 2FA, CAPTCHA, organization policy, or branch protection. Stop at such a boundary and tell the user what they must complete.
- Do not move an authenticated session between browsers. Use the browser where GitHub is already signed in.
- Scan the exact publish set for secrets and accidental files before any external write. Exclude `.git/`, `.env*`, private keys, credentials, editor state, caches, and `.DS_Store` unless the user deliberately requires a specific safe file.
- Preserve third-party licenses, copyright notices, source links, and modification notices. Do not claim third-party work as original.
- Treat repository deletion, history rewrites, visibility changes, and branch replacement as separate destructive operations that require explicit authorization.

## Choose the publishing route

1. Check for a purpose-built GitHub connector or an already-authenticated `gh` CLI first.
2. If it can perform the requested write without new authentication, prefer it.
3. If it is blocked by device login, Google/email access, or missing credentials and the user has an authenticated web session, use the browser UI.
4. If the user explicitly names Chrome or the in-app browser, obey that choice. Otherwise select the browser for the repository URL according to the available browser-control skill.
5. Read and follow the selected browser-control skill before browser work. Use its supported browser runtime only.

Do not restart a failed OAuth/device flow repeatedly when the user has asked to use the existing web session.

## Prepare the release

Resolve these values before writing:

- local source directory;
- exact relative paths to publish;
- GitHub owner and repository;
- target branch;
- destination subdirectory, if any;
- repository visibility;
- license and attribution requirements.

Use `rg --files -uu` or version-control metadata to enumerate files. Review names and sizes. Run a secret scan appropriate to the content. For a Git repository, `git ls-files` is the authoritative intended set when the user has staged or tracked the release.

For public repositories, run `scripts/verify_public_repo.py` after publication. It computes the same SHA-1 Git uses for blobs and compares the local tree with GitHub's public recursive tree API.

## Inspect the web session

- Navigate to the repository or GitHub home through the selected browser.
- Confirm the visible signed-in username and repository access from the page DOM. Do not inspect session storage.
- If the repository does not exist and creation is authorized, create it with the requested visibility and license choices.
- If creation or a sensitive setting triggers reauthentication, stop. A normal file commit may continue only when GitHub permits it through the current session.

## Publish files

Read [references/web-publishing-flow.md](references/web-publishing-flow.md) before performing browser publication or cleanup.

Core rules:

1. Inventory the remote tree first when updating an existing repository.
2. Skip files whose Git blob hashes already match.
3. Edit files that already exist; create only missing paths.
4. For every new text file, open GitHub's root-anchored `/<owner>/<repo>/new/<branch>` page before entering the full repository-relative path. Never start the next creation from a child directory.
5. Use GitHub's file upload UI for binary files. Do not paste binary data into the text editor.
6. Commit in small batches and verify the visible destination path after each batch.
7. Keep user-facing progress updates concise and report completed file counts.

The root-anchoring rule is mandatory. GitHub's “create file” action is relative to the current directory; reusing a child-directory page can silently create repeated paths such as `skills/x/skills/x/...`.

## Recover path drift

If a commit lands in the wrong directory:

1. Stop the current batch.
2. Obtain the exact remote blob paths from the public recursive tree API or the authenticated repository tree.
3. Distinguish correct files from incorrectly nested files using the local manifest.
4. Delete only the confirmed incorrect blob paths through GitHub's file deletion page and commit those deletions. Empty directories disappear automatically.
5. Recreate the missing files from the root-anchored create page.
6. Run a full path-and-hash comparison before proceeding.

Do not delete an entire repository or rewrite history merely to repair path drift.

## Verify completion

For a public repository, run:

```bash
python3 scripts/verify_public_repo.py LOCAL_DIR OWNER/REPO \
  --branch main \
  --remote-subdir OPTIONAL/PREFIX
```

Success requires all of the following:

- expected and remote file counts match within the selected scope;
- there are no missing, extra, or content-mismatched blobs;
- no repeated or unintended directory prefixes remain;
- repository visibility and default branch match the request;
- license and attribution files are present when required;
- the public repository URL opens without authentication when public visibility was requested.

For a private repository, do not pass credentials to the verifier. Compare paths and visible file contents through an authenticated GitHub connector or the existing browser session.

## Finish

- Leave the repository page open as the deliverable browser tab.
- Finalize browser tabs only after every verification step; finalization must be the last browser action.
- Report the repository URL, published subdirectories, file count, visibility, license, verification result, and any unresolved authentication boundary.
- State that no password, cookie, token, or verification code was read or stored.

Useful invocation examples:

- “Use `$github-publish` to publish these three local skills through my already logged-in GitHub webpage.”
- “GitHub CLI cannot finish Google verification. Use `$github-publish` to update my existing public skill repository without touching my credentials.”
- “Use `$github-publish` to verify that the files on GitHub exactly match this local skill folder.”
