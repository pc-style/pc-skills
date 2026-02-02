---
name: load-handoff
description: Load a handoff file and proceed with the specified tasks. Use when starting a new session with a HANDOFF.md file present, or when the user asks to continue from a handoff. Reads the handoff context and immediately begins executing the next steps.
---

# Load Handoff

Load HANDOFF.md and continue the work described.

## Process

1. **Read HANDOFF.md** from the repository root
2. **Load context files** listed in the handoff
3. **Confirm understanding** with the user briefly
4. **Execute next steps** or ask user which task to prioritize

## Steps

1. Check if `HANDOFF.md` exists in the current directory
2. If found, read it completely
3. Load all files listed in "Key Files" section
4. Present a brief summary:
   - What the handoff contains
   - Current state
   - 2-3 suggested next actions
5. Ask user which task to tackle or proceed if clear

## Example Interaction

```
[Reads HANDOFF.md and key files]

I've loaded the handoff. We're working on [context from handoff].

Current state: [state from handoff]

Suggested next steps:
1. [First next step from handoff]
2. [Second next step]
3. [Third next step]

Which would you like to tackle first?
```

## After Loading

Once handoff is loaded:
- Delete or archive HANDOFF.md after confirming work is complete
- Update progress as tasks are finished
- Create a new handoff if session ends with remaining work

## No Handoff Found

If no HANDOFF.md exists:
- Inform the user
- Ask what they'd like to work on
- Offer to create a handoff when session ends