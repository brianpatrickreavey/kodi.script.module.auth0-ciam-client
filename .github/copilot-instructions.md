# .github/copilot-instructions.md

Exploration is the default. Answer questions and design options in text. Change files when the user asks for a change or a result. A "?" does not cancel a request, and a missing "?" does not turn a speculative idea into a task.

## script.module.auth0-ciam-client

Kodi script module that wraps the `auth0-ciam-client` library. It is not `plugin.video.angelstudios`. Ship steps are in `~/Code/kodi-development/README.md`. Prefer `AGENTS.md` for this repo.

### Workflow Practices

- Exploration and implementation are different. A question, a comparison, a "what if", or a request to look at options is exploration: answer it and stop. Do not edit files, install software, or commit as a side effect of exploring.
- If one message mixes a concrete task with an open question, do the task and answer the question. Do not implement the answer in the same turn.
- When the scope is ambiguous, state the assumption and wait before changing files.
- Ask for clarification when several approaches are real options and the user has not picked one.
- All proposed code changes should be preceded by a clear plan and rationale.
- The developer controls the process; defer to their decisions.
- Always re-read all relevant files before making suggestions or changes. Do NOT rely on cache or other shortcuts.
- Never assume how something works—verify by reading files and documentation.
- Be truthful and factual; avoid anthropomorphism (e.g., do not claim to "misread" files or "forget" actions).
- Prioritize accurate, concise, and direct communication.
- Prioritize correct, robust code; avoid workarounds, shortcuts, or bad patterns.
- Project MUST achieve minimum 90% unit test coverage (target: 100% by v1.0.0), per `make unittest-with-coverage`
  - This exact command is preapproved.  Do not add any redirection or piping to the command above.
  - Any use of `# pragma: no cover` must be explicitly approved.
- Adhere to best practices; justify any deviations clearly.
- Use test data and parameterization extensively in tests.
- Favor verbose, readable code over clever or obscure implementations.