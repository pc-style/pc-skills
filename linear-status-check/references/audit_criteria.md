# Audit Criteria Reference

## Linear Status Mappings

### "Done" Statuses
Issues with these statuses should have corresponding code in the repository:
- Completed
- Done
- Deployed
- Merged
- Closed (if marked as completed, not cancelled)

### "In Progress" Statuses
Issues with these statuses may or may not have code:
- In Progress
- In Review
- In Testing
- Blocked

### "Not Started" Statuses
Issues with these statuses should NOT have implementation code:
- Backlog
- To Do
- Todo
- Planned

## Verification Criteria

### What Counts as "Implemented"

An issue is considered implemented if:
1. **Merged PRs** exist that reference the issue (by title, ID, or description)
2. **Commits** exist that reference the issue and include actual code changes
3. **Code exists** that implements the described functionality (verified by file changes, not just commit messages)

### Red Flags

**False Positives** (marked done but not implemented):
- Issue marked "Completed" but no matching commits/PRs
- Commits exist but only contain trivial changes (comments, formatting)
- PR exists but was reverted or didn't actually implement the feature

**False Negatives** (implemented but not marked):
- Code exists for functionality but issue still in "To Do" or "In Progress"
- PR merged but Linear issue not updated

## Audit Output Structure

The audit should include:

1. **Sync Status Summary**
   - Total issues checked
   - Issues in sync
   - Issues out of sync (with breakdown)

2. **Detailed Findings**
   - Issues marked done but not implemented (with evidence)
   - Issues implemented but not marked done (with evidence)
   - Issues in review with code ready

3. **Recommended Next Steps**
   - Priority order for implementing missing features
   - Issues that need status updates
   - Potential cleanup tasks

4. **Claude Code Prompts**
   - Copy-paste ready prompts for each actionable issue
   - Include full context: issue description, acceptance criteria, related files
   - Suggest implementation approach based on existing codebase patterns
