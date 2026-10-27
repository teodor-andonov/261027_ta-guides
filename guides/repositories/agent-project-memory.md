# Agent project memory

This guide explains the personal default for durable project context across coding agents and chats. Adapt the level of recordkeeping to each project rather than treating it as a corporate policy. The [copyable template](../../templates/repository/) is self-contained.

---

`logs/` preserves context across chats, agents, and interruptions. Capture **why, what, results, and next steps**, not raw transcripts or noise. Code is the truth for implementation; logs preserve plans, reasoning, and evidence.

## Structure

| Path | Purpose |
| --- | --- |
| `status.md` | Current state, blockers, next action; keep short |
| `roadmap.md` | Planned / active / verified done / blocked work |
| `decisions.md` | Important decisions, alternatives, rationale, reversals |
| `knowledge.md` | Reusable findings, comparisons, constraints, open questions |
| `sessions/` | Dated discussions, implementation, experiments, tests |
| `visuals/` | Screenshots, diagrams, UI comparisons and visual evidence |

Outside `logs/`: `tests/` holds **test source code**; `test-artifacts/` holds **disposable generated test results** (usually gitignored). Do not create vague `outputs/` folders. Curate useful evidence into `logs/visuals/` and link it from a session note.

## Naming (required)

Name every **new note, session, screenshot, diagram, exported visual, report, or other agent-generated record/artifact**:

`YYMMDD-HHmm_short-descriptive-name.ext`

Examples: `261015-1114_header-layout.md`, `261015-1122_header-desktop.png`. The timestamp is the file's **original creation time** (project-local time; UTC if unknown), **not** the time it was edited, committed, or moved. Keep the original timestamp on edits. If names collide, append `-02`, `-03`, etc. One-off experiment folders also use this prefix when useful.

Exceptions: canonical source/config filenames, category folders, and stable entry points/living trackers (`AGENTS.md`, `README.md`, `status.md`, `roadmap.md`, `decisions.md`, `knowledge.md`, etc.) retain their conventional names. Do not timestamp `index.html`, `package.json`, or normal application code.

## Visual evidence (required)

**For every user prompt that builds, changes, or reviews something visual, save at least one new screenshot of the actual rendered result.** Do this per prompt, not merely once per session or milestone.

- Capture the relevant state after work; include additional views/breakpoints if useful.
- Save to `logs/visuals/` with the creation-time filename; link it in the corresponding session record and briefly say what it shows.
- Screenshots of failed or intermediate states are welcome when informative.
- A generated mockup is not proof that a running UI works. If screenshots cannot be captured, state why and mark visual validation **not done**; never invent evidence.

## Working loop

1. **Start:** Read `status.md` and `roadmap.md`, then relevant decisions/sessions. Inspect real files before assuming a feature exists.
2. **Discuss/plan:** Record meaningful questions and answers, ideas, constraints, rejected options, unresolved issues, and decisions. Distinguish proposal from agreement.
3. **Build/test:** Record meaningful changes, touched paths, deviations, test commands/results, limitations, and visual evidence. Update roadmap statuses only when verified.
4. **Handover:** Update `status.md` and `roadmap.md`; append significant decisions/knowledge; leave a dated `sessions/` record with concise context, work, results, screenshots, and next steps. Save checkpoints during long tasks.

A session can cover several prompts; identify which visual screenshot belongs to each visual prompt. Prefer links to repeated prose. Preserve historical sessions; update living trackers in place. Never erase a superseded decision without leaving its history. Never claim work, testing, or earlier context you cannot verify.

## Minimal session note

```md
# Topic
Created: YYYY-MM-DD HH:mm (timezone)
Context / question:
Discussion / alternatives / decision:
Work / affected paths:
Validation / findings:
Visuals: [screenshot](../visuals/YYMMDD-HHmm_name.png)
Open issues / next step:
```

Omit inapplicable fields. The goal is fast onboarding and reliable history, **not documentation bureaucracy**.
