# GitHub web publishing flow

Use this reference only after the core skill has selected browser publication.

## Contents

1. Preflight inventory
2. Browser setup and repository inspection
3. Create and edit operations
4. Binary files
5. Batch control
6. Path-drift recovery
7. Verification
8. Failure matrix

## 1. Preflight inventory

Build an exact repository-relative manifest before opening an editor.

- Prefer `git ls-files` for a prepared Git source tree.
- Otherwise enumerate with `rg --files -uu` and explicitly exclude `.git/`, caches, editor files, `.DS_Store`, credentials, and build artifacts that are not part of the release.
- Record each path, byte size, text/binary status, and Git blob SHA.
- Inspect `.env*`, key files, token-like strings, private URLs, personal data, and generated files before publication.
- Confirm third-party license and notice files travel with copied or modified work.

The verifier bundled with this skill computes Git blob SHA values for ordinary files. Symlinks and submodules require a Git-aware publishing route and should not be flattened silently through the web editor.

## 2. Browser setup and repository inspection

Follow the selected browser-control skill exactly. Reuse a live browser binding and a live tab when available. Read the browser's full runtime documentation before first interaction.

Inspect visible DOM state before clicking. Prefer role/name locators over coordinates. Account for GitHub interface language changes by checking the visible labels instead of assuming Chinese or English.

Verify:

- the visible GitHub username;
- repository owner/name;
- `Public` or `Private` status;
- current branch;
- existing file tree;
- write access through ordinary repository controls.

Do not inspect cookies, local storage, browser profiles, password managers, or developer storage panels.

## 3. Create and edit operations

### Create a missing text file

Anchor every operation at the repository root:

```text
https://github.com/OWNER/REPO/new/BRANCH
```

Then:

1. Inspect the page and locate the file-name field and content editor.
2. Fill the file-name field with the full repository-relative path, for example `skills/example/SKILL.md`.
3. Fill the text editor with the exact local content.
4. Open the commit dialog.
5. Use an intentional commit message such as `Add skills/example/SKILL.md`.
6. Commit to the authorized branch.
7. Wait until the dialog closes and the page shows the expected file or parent directory.
8. Check the resulting breadcrumb/path before starting another file.

Do not enter the next path from a page such as:

```text
https://github.com/OWNER/REPO/tree/BRANCH/skills/example
```

GitHub treats “create file” from that page as relative to `skills/example`, so filling `skills/example/SKILL.md` can create `skills/example/skills/example/SKILL.md`.

### Edit an existing text file

Use the exact edit route or the visible Edit action:

```text
https://github.com/OWNER/REPO/edit/BRANCH/FULL/PATH
```

Compare the existing Git blob SHA first. Skip the edit when content already matches. Preserve final newlines and encoding.

### Delete a confirmed wrong file

Use the exact deletion route or visible Delete action:

```text
https://github.com/OWNER/REPO/delete/BRANCH/FULL/WRONG/PATH
```

Confirm the page heading identifies the exact file. Commit a narrow message such as `Remove incorrectly nested file`. Delete blobs one by one unless an authenticated Git-aware route can safely commit the same explicit deletion set. Git removes the now-empty directory automatically.

### Selector guidance

The exact browser API varies by runtime. Prefer this sequence:

1. inspect DOM snapshot;
2. locate by accessible role and exact visible name;
3. count matches before using positional selection;
4. use the editor's two textboxes only after confirming their order from DOM state;
5. scope commit fields and buttons to the commit dialog;
6. wait for dialog closure and navigation;
7. inspect the resulting breadcrumb.

Do not rely on a previous page's current directory, a fixed language, or pixel coordinates.

## 4. Binary files

Classify files before browser publication.

- Text, Markdown, YAML, JSON, Python, shell, small SVG, and similar UTF-8 files can use the text editor.
- Images, archives, fonts, PDFs, office documents, and other binary files must use GitHub's Upload files flow or another authenticated Git-aware route.
- If the browser runtime cannot operate the file chooser reliably, stop and report the exact binary paths still pending. Do not base64 them into repository text unless the repository format explicitly requires that representation.
- Respect GitHub's current size limits and Git LFS requirements.

## 5. Batch control

- Publish five to eight small text files per batch when using repeated browser commits.
- Use fewer files for large content or slow page transitions.
- Keep a local completed-path list based on confirmed commits, not attempted operations.
- After each batch, re-open the repository root or a known directory and inspect the tree.
- Provide a concise progress update before a browser operation is likely to exceed one minute.
- If one item fails, stop the batch and inspect the current page. Do not blindly continue.

## 6. Path-drift recovery

Path drift commonly appears as repeated segments:

```text
skills/example/skills/example/...
```

Recovery procedure:

1. Stop creating files.
2. Fetch the recursive tree for a public repository:

   ```text
   https://api.github.com/repos/OWNER/REPO/git/trees/BRANCH?recursive=1
   ```

3. Extract blob paths and compare them with the local manifest.
4. Reconstruct the exact accidental paths from the remote tree; never guess from the visible directory alone.
5. Delete only paths absent from the intended manifest.
6. Return to `https://github.com/OWNER/REPO/new/BRANCH` before recreating each missing file.
7. Run the verifier after cleanup.

Do not repair by deleting the repository, force-pushing, resetting branches, or rewriting history unless the user separately authorizes that destructive action.

## 7. Verification

For a public repository, use the bundled verifier from the skill directory:

```bash
python3 scripts/verify_public_repo.py /absolute/local/path OWNER/REPO \
  --branch main
```

To compare one local skill against a subdirectory in a larger repository:

```bash
python3 scripts/verify_public_repo.py /absolute/local/skill OWNER/REPO \
  --branch main \
  --remote-subdir skills/skill-name
```

Exit code `0` means paths and blob hashes match. Exit code `1` means missing, extra, or mismatched files. Exit code `2` means validation could not run, commonly because the repository is private, the API is unavailable, or input is invalid.

After content verification, confirm repository metadata separately:

- visibility;
- default branch;
- license identifier;
- public unauthenticated access when public visibility was requested.

The public API may cache metadata briefly after rapid web commits. Retry the read-only check after a short interval if the visible repository is newer than the API response.

## 8. Failure matrix

| Condition | Action |
|---|---|
| GitHub asks for password, email code, Google login, 2FA, passkey, or CAPTCHA | Stop and ask the user to complete it in the selected browser. Do not switch surfaces to evade it. |
| CLI/device login is blocked but ordinary web commits work | Continue through the already-authenticated web UI. Do not request or extract credentials. |
| Browser is signed into the wrong GitHub account | Stop and report the visible username. Do not log out or switch accounts without user direction. |
| Repository creation triggers sudo mode | Stop; do not create the repository by another route unless the user authenticates or chooses an existing repository. |
| A normal commit succeeds but the page stays in a child directory | Navigate explicitly to the root create URL before the next file. |
| The remote tree contains unexpected files | Do not delete them automatically. Delete only files proven to have been created by the current failed batch and absent from the intended manifest. |
| Public API returns 404 for a private repository | Verify through the authenticated connector or browser. Never append credentials to a command or URL. |
| Branch protection rejects direct commits | Use the permitted branch/PR workflow or ask the user; do not disable protection. |
| Binary file chooser is unavailable | Report the pending binary paths and use a supported authenticated route after user direction. |
