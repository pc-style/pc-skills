---
name: git-push-origin
description: Push local branch to origin (GitHub) to initialize it remotely. Use when the user has created a local branch and wants to push it to GitHub for the first time, or when setting up a new branch on the remote repository.
---

# Git Push Origin

Push a local branch to origin to initialize it on the remote (GitHub).

## When to Use

- New branch needs to exist on GitHub
- First push of a local branch
- Setting up remote tracking
- Any request to "push branch to origin" or "init branch on GitHub"

## Workflow

### 1. Check Current State

```bash
git status
git branch --show-current
git remote -v
```

### 2. Push with Upstream Tracking

**First push (initialize on origin):**
```bash
git push -u origin <branch-name>
```

Or using the current branch:
```bash
git push -u origin HEAD
```

### 3. Verify Remote Branch

```bash
git branch -vv
git log --oneline --graph --decorate -5
```

## Common Scenarios

**Push current branch for the first time:**
```bash
git push -u origin HEAD
```

**Push specific branch:**
```bash
git push -u origin feature/my-feature
```

**Push after making commits:**
```bash
git add .
git commit -m "feat: initial implementation"
git push -u origin HEAD
```

## What `-u` (Upstream) Does

The `-u` flag sets up tracking between local and remote branch:
- Future pushes can use just `git push`
- Future pulls can use just `git pull`
- Shows tracking info in `git branch -vv`

## Best Practices

- Always use `-u` on first push to set upstream
- Push after initial commit(s) to back up work
- Verify branch appears on GitHub
- Ensure you're on the correct branch before pushing