---
name: github-create-pr
description: Create a GitHub Pull Request using the gh CLI. Use when the user wants to open a PR, submit changes for review, or create a pull request from their branch. Handles PR creation with title, body, and target branch selection.
---

# GitHub Create PR

Create a GitHub Pull Request using the `gh` CLI.

## When to Use

- Ready to submit changes for review
- Need to create a pull request
- Any request to "open PR", "create PR", or "submit for review"

## Prerequisites

Ensure `gh` CLI is installed and authenticated:
```bash
gh --version
gh auth status
```

If not authenticated:
```bash
gh auth login
```

## Workflow

### 1. Check Branch Status

```bash
git status
git branch --show-current
git log --oneline -5
```

### 2. Push Branch (if needed)

```bash
git push -u origin HEAD
```

### 3. Create the PR

**Quick creation with defaults:**
```bash
gh pr create
```

**With custom title:**
```bash
gh pr create --title "feat: add user authentication"
```

**With title and body:**
```bash
gh pr create --title "feat: add user authentication" --body "Implements OAuth2 login flow with support for Google and GitHub providers."
```

**Fill from commit messages:**
```bash
gh pr create --fill
```

**Target specific base branch:**
```bash
gh pr create --base main
```

### 4. Copy PR URL

After creation, the PR URL is printed. You can also get it with:
```bash
gh pr view --json url --jq '.url'
```

## Common Options

| Flag | Description |
|------|-------------|
| `--title` | PR title |
| `--body` | PR description |
| `--fill` | Use commit message as title/body |
| `--base` | Target branch (default: repo default) |
| `--head` | Source branch (default: current) |
| `--draft` | Create as draft PR |
| `--label` | Add labels |
| `--assignee` | Assign to user(s) |
| `--reviewer` | Request reviewer(s) |

## Examples

**Create draft PR:**
```bash
gh pr create --draft --title "WIP: refactor API"
```

**Add labels and reviewer:**
```bash
gh pr create --title "fix: resolve memory leak" --label "bug" --reviewer "@username"
```

**Use template:**
```bash
gh pr create --template="feature.md"
```

## Best Practices

- Push branch before creating PR
- Write clear, descriptive titles
- Include context in body (what changed, why)
- Reference related issues: `Closes #123`
- Add appropriate labels
- Request reviewers
- Use draft PRs for work-in-progress