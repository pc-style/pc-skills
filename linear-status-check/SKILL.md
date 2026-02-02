---
name: linear-status-check
description: Audit Linear project status against GitHub repository state to identify sync issues and generate actionable next steps. Use for checking if Linear issues match actual code implementation, finding discrepancies between marked status and reality, and creating detailed prompts for coding tools like Claude Code.
license: MIT
---

# Linear Status Check

Audit Linear project issues against GitHub repository state to verify sync between tracked status and actual implementation.

## When to Use

Use this skill when:
- User requests a status check or audit of a Linear project
- User wants to verify if Linear issues match the actual codebase
- User needs to identify what's marked done but not implemented (or vice versa)
- User wants actionable next steps with prompts for coding tools

## Workflow

### 1. Identify Project and Repository

**Auto-detect from context:**
- Check user's GitHub integration for selected repositories
- Search Linear for projects matching keywords in the conversation
- Look for explicit mentions of project or repo names

**If ambiguous, ask:**
- "Which Linear project should I audit?"
- "Which GitHub repository should I check?"

For the user pcstyle, common mappings:
- Project: "odrodzenie oddechowe" (or similar) → Repo: `pc-style/oddech`

### 2. Fetch Linear Issues

Use `manus-mcp-cli` to interact with Linear MCP server:

```bash
# List available tools
manus-mcp-cli tool list --server linear

# Search for project
manus-mcp-cli tool call search_projects --server linear --input '{"query": "project_name"}'

# Get issues for a project
manus-mcp-cli tool call search_issues --server linear --input '{"project_id": "PROJECT_ID"}'
```

Focus on issues with these statuses:
- **Done statuses**: Completed, Done, Deployed, Merged, Closed
- **In-progress statuses**: In Progress, In Review, In Testing
- **Backlog statuses**: To Do, Backlog, Planned

### 3. Clone and Analyze Repository

Clone the repository if not already present:

```bash
gh repo clone <repo-name> /home/ubuntu/repos/<repo-name>
```

Use the bundled script to analyze implementation status:

```bash
python3 /home/ubuntu/skills/linear-status-check/scripts/analyze_repo.py \
  /home/ubuntu/repos/<repo-name> \
  "keyword1" "keyword2" "keyword3"
```

The script returns JSON with:
- `commits`: Matching commits with file changes
- `prs`: Merged PRs referencing the keywords
- `has_activity`: Boolean indicating if any activity found

**Extract keywords from Linear issues:**
- Issue title (primary)
- Issue identifier (e.g., "ODD-123")
- Key terms from description

### 4. Cross-Reference and Identify Discrepancies

For each issue, determine sync status:

**In Sync:**
- Status = "Done" AND code exists (commits/PRs with actual changes)
- Status = "To Do" AND no code exists

**Out of Sync:**
- Status = "Done" BUT no code exists → **False positive**
- Status = "To Do" BUT code exists → **False negative**
- Status = "In Review" BUT no recent activity → **Stale**

**Verification depth:**
- Don't just check commit messages (someone can write "build auth" without actually doing it)
- Check file changes: look for actual implementation files, not just docs or config
- For "done" issues, verify the code actually implements the described functionality

### 5. Generate Audit Report

Use the template at `/home/ubuntu/skills/linear-status-check/templates/audit_report_template.md`.

**Report sections:**

1. **Executive Summary**: High-level overview (2-3 sentences)

2. **Sync Status Overview**: Table with counts

3. **Detailed Findings**:
   - **Marked Done but Not Implemented**: List issues with evidence (no commits/PRs, or trivial changes only)
   - **Implemented but Not Marked**: List issues with evidence (commits/PRs exist, but status not updated)
   - **In Review with Code Ready**: Issues that might be ready to merge

4. **Recommended Next Steps**: Priority-ordered list of actions:
   - Issues to implement (highest priority first)
   - Issues needing status updates
   - Potential cleanup or refactoring

5. **Claude Code Prompts**: Copy-paste ready prompts for each actionable issue:
   - Include full issue context (title, description, acceptance criteria)
   - Describe what needs to be implemented
   - Suggest files or patterns to follow based on existing code
   - Provide technical context (since Claude Code won't have Linear access)

**Example prompt format:**

```
### Issue: [ODD-15] Implement user authentication

**Context:**
This issue is marked as "To Do" in Linear but needs implementation. The project uses [tech stack details]. Authentication should follow [pattern/approach].

**Requirements:**
- [Requirement 1 from Linear]
- [Requirement 2 from Linear]
- [Requirement 3 from Linear]

**Suggested Implementation:**
1. Create auth service in `src/services/auth.ts`
2. Add middleware for route protection
3. Implement login/logout endpoints
4. Add JWT token handling

**Related Files:**
- `src/services/` (existing services for reference)
- `src/middleware/` (middleware patterns)
- `src/routes/api.ts` (API route structure)

**Prompt for Claude Code:**
"Implement user authentication for the application. Create an auth service that handles login, logout, and JWT token management. Add middleware to protect routes. Follow the existing service patterns in src/services/ and integrate with the API routes in src/routes/api.ts. Use bcrypt for password hashing and jsonwebtoken for token generation."
```

### 6. Deliver Report

Save the report to `/home/ubuntu/linear_audit_report.md` and send it to the user via `message` tool with attachment.

## Reference Documents

- **Audit Criteria**: See `/home/ubuntu/skills/linear-status-check/references/audit_criteria.md` for detailed status mappings and verification criteria

## Tips

- Be thorough but concise: focus on actionable discrepancies
- When checking "done" issues, look for substantive code changes, not just commit messages
- For Claude Code prompts, include enough context that someone without Linear access can implement the feature
- If the repository is large, focus on recent activity (last 90 days) to keep analysis manageable
- Update Linear issue statuses directly if user confirms the findings
