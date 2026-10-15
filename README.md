# TA Repo Guidance

Lightweight, reusable conventions for AI-agent projects: preserve reasoning, track work, and capture visual evidence without filling agent context with unnecessary documentation.

## Apply to another repository

1. Ask your agent to read [the project convention](template/logs/README.md).
2. Copy `template/AGENTS.md` and the contents of `template/logs/` into the target repository (merge with existing instructions instead of overwriting).
3. Create `logs/sessions/` and `logs/visuals/` as needed. Use `test-artifacts/` for disposable automated test results and ignore it in Git.
4. Adapt the trackers to the project's actual state. Do not invent past work or imply unverified tests passed.

**Suggested agent prompt**

> Follow https://github.com/teodor-andonov/ta-repo-guidance. Read the convention and apply it to this repository, preserving existing content and compatible instructions. Keep guidance concise. For visual work, capture at least one screenshot of the actual rendered result per user prompt. Maintain project memory during development.

## What lives where

- `AGENTS.md` — brief instructions agents automatically discover.
- `logs/status.md` — current handoff; `logs/roadmap.md` — work plan.
- `logs/decisions.md` and `logs/knowledge.md` — durable reasoning and findings.
- `logs/sessions/` — timestamped discussions and development records.
- `logs/visuals/` — timestamped screenshots and visual evidence.
- `tests/` — test *source code*; `test-artifacts/` — disposable test-generated results.

The timestamp rule is `YYMMDD-HHmm_short-descriptive-name.ext`, using **creation time**, not the time a file was last edited. Canonical entry points and living trackers keep stable names.

[Read the full compact convention →](template/logs/README.md)
