---
name: create-handoff
description: Create a handoff message to continue work in a new AI session. Use when the user wants to save context for later, create a handoff document, or prepare work for continuation in a fresh session. Captures relevant files, context, and goals so the next session can start immediately without rediscovering the codebase.
---

# Create Handoff

Generate a HANDOFF.md file to preserve context for the next AI session.

## When to Use

- User says "let's continue later"
- User asks to save current progress
- Session is ending but work is incomplete
- User explicitly asks for a handoff

## Process

1. **Identify relevant files** (target 8-15 files, up to 20 for complex work)
   - Files being edited or will be edited
   - Dependencies and imports
   - Relevant tests
   - Configuration files
   - Key reference documentation

2. **Draft context and goals**
   - What we're working on
   - Current state and progress
   - Decisions made
   - Constraints and preferences
   - Technical patterns discovered
   - Next steps or remaining tasks

3. **Exclude**
   - Conversation back-and-forth
   - Dead ends and failed attempts
   - Meta-commentary
   - File contents (just list paths)

## Output Format

Save to `HANDOFF.md` in the repository root:

```markdown
# Handoff: [Brief Title]

## Context
[What we're building/fixing and why]

## Current State
[What's been done, what's in progress]

## Key Files
- `path/to/file.ts` - [why it matters]
- `path/to/test.ts` - [relevant tests]
[8-15 files with brief descriptions]

## Decisions & Constraints
- [Decision made]
- [User preference]
- [Technical constraint]

## Next Steps
1. [Specific task]
2. [Specific task]
```

## Tips

- Be generous with files - cost is low, missing critical files is high
- Preserve user preferences exactly as stated
- Focus on actionable next steps
- Keep it scannable - bullet points over paragraphs