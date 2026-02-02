---
name: generate-agents-md
description: Generate AGENTS.md file for a codebase to help AI agents understand the project structure, build commands, testing, and conventions. Use when the user asks to create an AGENTS.md, initialize agent documentation, or analyze a codebase for agent context. Also use when setting up a new repository for AI-assisted development.
---

# Generate AGENTS.md

Generate an AGENTS.md file containing essential information for AI agents working in this repository.

## What to Include

The AGENTS.md file should be ~20 lines and contain:

1. **Build/lint/test commands** - Especially how to run a single test
2. **Architecture overview** - Important subprojects, internal APIs, databases
3. **Code style guidelines** - Imports, conventions, formatting, types, naming, error handling

## Process

1. First check if AGENTS.md or AGENT.md already exists - if so, update it instead of overwriting
2. Check for existing rules files to incorporate:
   - `.cursor/rules/` or `.cursorrules`
   - `CLAUDE.md`
   - `.windsurfrules`
   - `.clinerules`
   - `.goosehints`
   - `.github/copilot-instructions.md`
3. Analyze the codebase structure:
   - Look at package.json, Cargo.toml, pyproject.toml, etc.
   - Identify test frameworks and commands
   - Find lint/format configuration files
   - Map out the directory structure
4. Write concise AGENTS.md (~20 lines)

## Output

Save the generated file as `AGENTS.md` in the repository root.

## Example Structure

```markdown
# Agent Guidelines

## Commands
- Build: `npm run build`
- Test: `npm test` (single: `npm test -- file.test.ts`)
- Lint: `npm run lint`

## Architecture
- Monorepo with packages in `/packages/`
- Main API in `/packages/api/`
- Database: PostgreSQL with Prisma

## Style
- TypeScript with strict mode
- ESLint + Prettier
- Named exports preferred
- Use `logger` from `@/utils` not console
```