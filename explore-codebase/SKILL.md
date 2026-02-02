---
name: explore-codebase
description: Fast codebase exploration using Opencode's Explore agent for quick recognition of project structure, file patterns, and code organization. Use when you need to understand a codebase quickly, map out architecture, find files by patterns, or answer questions about code structure. Triggers on requests like "explore this codebase", "understand the project structure", "map out the architecture", or when quick file discovery is needed.
---

# Explore Codebase

Use Opencode's built-in **Explore agent** for fast, read-only codebase exploration.

## When to Use

- Initial codebase discovery and mapping
- Finding files by patterns (e.g., "find all React components")
- Understanding project structure and architecture
- Quick code searches without modifying files
- Answering questions about "where is X located?"

## How to Use

### Option 1: Invoke @explore Subagent

When running inside Opencode, invoke the Explore subagent directly:

```
@explore Find all API endpoints in this codebase
```

```
@explore Map out the database models and their relationships
```

```
@explore What authentication patterns are used here?
```

### Option 2: CLI with Explore Agent

From the terminal, use the `--agent explore` flag:

```bash
opencode run --agent explore "Map out the project structure"
```

```bash
opencode run --agent explore "Find all test files"
```

```bash
opencode run --agent explore "What are the main components in src/?"
```

## What Explore Agent Does

The Explore agent is:
- **Read-only** - Cannot modify files (safe for exploration)
- **Fast** - Optimized for quick searches and file discovery
- **Pattern-matching** - Great for glob searches and keyword finding
- **Codebase mapping** - Efficient at understanding structure

## Common Patterns

**Map entire codebase:**
```
@explore Give me an overview of this project's architecture
```

**Find specific files:**
```
@explore Find all files related to authentication
```

**Understand patterns:**
```
@explore What testing framework is used and where are tests located?
```

**Quick search:**
```
@explore Search for where 'User' type is defined
```

## Best Practices

1. **Start broad, then narrow** - Ask for overall structure first
2. **Use specific terms** - Name files, functions, or patterns explicitly
3. **Chain explorations** - Use results to ask follow-up questions
4. **Combine with other agents** - After exploring, switch to Build agent to make changes

## Integration with Workflow

After exploring, transition to implementation:

```
@explore [your exploration query]

[Review results, then:]

Now let's implement the changes. [Switch to Build agent or continue with main agent]
```