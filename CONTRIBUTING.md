# Contributing to ESC Skills

Thanks for your interest in contributing to ESC Skills! This guide covers how to create and submit new skills.

## Skill Structure

Every skill lives in `skills/<skill-name>/` and contains at minimum:

```
skills/my-skill/
├── SKILL.md          # Main instruction file (required)
└── references/       # Optional supporting files
    ├── examples.md
    ├── templates/
    └── ...
```

## SKILL.md Format

Every `SKILL.md` must follow this structure:

```markdown
<!-- skill: skill-name | version: 1.0.0 | updated: YYYY-MM-DD -->
---
name: skill-name
description: >
  One-paragraph description of what this skill does and when it should be triggered.
  Include trigger keywords for agent auto-detection.
---

# skill-name

Brief overview of the skill's purpose.

## [Main Sections]

Step-by-step instructions, prompts, quality criteria, and output specs.

## Referências / References

Links to files in the `references/` directory.
```

## Required Sections

| Section | Purpose |
|---------|---------|
| **Frontmatter** | YAML with `name` and `description` (including trigger keywords) |
| **Overview** | What the skill does in 1-2 sentences |
| **Workflow/Process** | Step-by-step instructions the agent should follow |
| **Quality Criteria** | How to validate output quality |
| **Output** | Expected deliverables and their formats |

## Optional Sections

| Section | When to Include |
|---------|----------------|
| **⚠️ Known Limitations** | If the skill has domain-specific constraints agents should disclose |
| **📋 Output Examples** | If real outputs exist in the showcase |
| **References** | If the skill uses templates, examples, or base data |
| **HTML Output** | If the skill generates client-facing HTML deliverables |

## Naming Conventions

- **Skill directory:** `kebab-case` (e.g., `guimkt-google-ads`)
- **Proprietary marketing skills:** prefix with `guimkt-`
- **Reference files:** descriptive names in `references/` directory

## Quality Checklist

Before submitting, verify:

- [ ] `SKILL.md` has valid YAML frontmatter with `name` and `description`
- [ ] Description includes trigger keywords for agent auto-detection
- [ ] Instructions are specific enough for an AI agent to follow without ambiguity
- [ ] Quality criteria are measurable (not vague like "make it good")
- [ ] Output format is clearly specified
- [ ] No hardcoded paths, API keys, or sensitive data
- [ ] References directory contains only files actually referenced in SKILL.md
- [ ] Tested with at least one AI agent (Claude, Gemini, GPT, Cursor, etc.)

## Testing Your Skill

1. Copy your skill to `.agent/skills/` in any project
2. Ask an AI agent to execute it with a realistic briefing
3. Verify the output matches your quality criteria
4. Check edge cases (vague briefing, multi-brand scenario, etc.)

## Submitting

1. Fork the repository
2. Add your skill in `skills/<skill-name>/`
3. Test with at least one AI agent
4. Open a Pull Request with:
   - Skill name and purpose
   - Which agent(s) you tested with
   - Example output (or link to showcase)

## Code of Conduct

- Skills must produce **real, usable output** — not generic filler
- Be honest about limitations — add a Known Limitations section when relevant
- Don't claim capabilities the skill doesn't have
- Keep instructions agent-agnostic (works with any AI that reads files)
