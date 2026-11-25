# docs-code-tester

An agent skill that tests the code samples in Markdown documentation. It extracts every fenced code block from a docs page, checks each one against the real SDK and the package registries, and reports which samples fail and why.

It's built for docs sites that publish Markdown versions of their pages, like [LiveKit's](https://docs.livekit.io/llms.txt). Point it at one page, or at an `llms.txt` index to sweep an entire section.

- [`SKILL.md`](SKILL.md): instructions for a coding agent, covering setup, running, reading results, and verifying failures before reporting them.
- [`scripts/test_code_blocks.py`](scripts/test_code_blocks.py): the checker. One file, standard library only, Python 3.9+.
- [`findings/`](findings/): raw output from a sweep of LiveKit's Agents and Testing docs.

## Findings: LiveKit Agents and Testing docs

On November 24, 2026, I swept every page in the [Build Agents](https://docs.livekit.io/agents/llms.txt) and [Test & Evaluate](https://docs.livekit.io/testing/llms.txt) sections: **226 pages and 1,579 code blocks**. I ran the sweep against `livekit-agents` 1.8.13, the latest release on PyPI, with the `mcp` extra installed, on Python 3.14.

The script flagged 7 blocks. I reproduced each one by hand. Six are real problems; the seventh was a false positive, described under "What it got wrong".

### Samples that break when copied

| Page | What the sample does | What happens | Fix |
|---|---|---|---|
| [Instructions › Customize built-in tasks](https://docs.livekit.io/agents/multimodality/instructions.md) | `from livekit.agents.beta.workflows import GetEmailTask, InstructionParts` | `ImportError: cannot import name 'InstructionParts'`. It isn't in 1.8.13 or on the SDK's `main` branch. | The class is `WorkflowInstructions`. It takes the same `persona=` and `extra=` arguments the sample uses. |
| [Pipeline nodes › Realtime audio output node](https://docs.livekit.io/agents/logic/nodes.md) | `from livekit.agents import ModelSettings, rtc, Agent` | `ImportError: cannot import name 'rtc' from 'livekit.agents'` | `from livekit import rtc` |
| [Events reference › Continue after an error](https://docs.livekit.io/reference/agents/events.md) | `from livekit.agents import ErrorEvent, llm, multimodal, stt, tts`, then `multimodal.RealtimeModel` | `ImportError: cannot import name 'multimodal' from 'livekit.agents'` | Drop `multimodal` and use `llm.RealtimeModel`, which exists. |
| [Voice AI quickstart › Install the LiveKit CLI › From Source](https://docs.livekit.io/agents/start/voice-ai.md). The same block appears in [Google integration](https://docs.livekit.io/agents/integrations/google.md) and the [CLI reference](https://docs.livekit.io/reference/developer-tools/livekit-cli.md). | `git clone github.com/livekit/livekit-cli`, then `make install` | Without a scheme, git treats the address as a local path: `fatal: 'github.com/livekit/livekit-cli' does not appear to be a git repository`. `make install` also runs outside the cloned directory. | `git clone https://github.com/livekit/livekit-cli`, then `cd livekit-cli`, then `make install` |

The second, third, and fourth findings are typical API drift: the module layout changed and the samples didn't. The first may be docs written ahead of a release, but either way a reader on the current release can't run it.

### Problems a reader would hit

- **zsh rejects an install command.** [MCP › Overview](https://docs.livekit.io/agents/logic/tools/mcp.md) shows `uv add livekit-agents[mcp]~=1.8` with no quotes. In zsh, the macOS default shell, the brackets are a glob pattern, so the command fails with `zsh: no matches found: livekit-agents[mcp]~=1.8`. Quote it: `uv add 'livekit-agents[mcp]~=1.8'`.
- **A missing comma.** [Server options › Permissions](https://docs.livekit.io/agents/server/options.md) has `AgentServer(` with `...` on one line and `permissions=WorkerPermissions(...)` on the next. Python reads that as `... permissions=...` and raises a syntax error: "Perhaps you forgot a comma?". `...,` fixes it.
- **Program output tagged as `shell`.** Two "Verbose output" blocks on [Testing › Unit tests](https://docs.livekit.io/testing/unit-tests.md) show pytest and Vitest output, but they're tagged `shell`. So a copy button or a coding agent will offer to run them.
- **Shell commands tagged `text`.** 16 install and CLI blocks on the quickstart, the Google integration page, and the CLI reference use a `text` fence. On the same pages, other commands use `shell`. Readers lose syntax highlighting, and tools can't tell the block is runnable.

### Deliberate fragments

Seven Python blocks don't parse as pasted because they're intentional excerpts: a `# ...` body, `<human-agent-phone-number>`, or `...` standing in for other arguments. That's a normal docs convention, so the script reports them as notes rather than failures. On a site that wants copy-paste-safe samples, these are the candidates. For example, `sip_call_to="+15105550100"` would run where `sip_call_to=<human-agent-phone-number>` can't.

### What it got wrong, and how I fixed it

The first sweep flagged about 290 blocks. Almost all of them were false positives, and each became a fix in the script:

| False positive | Cause | Fix |
|---|---|---|
| `from livekit.plugins import openai` "fails" about 200 times | Plugins are separate packages, and `livekit.plugins` is a namespace package | Imports from a namespace package are reported as `env` (not installed), not `fail` |
| `lk agent simulate view <run-id>` "has a syntax error" | `<run-id>` reads as a redirection in bash | `<placeholders>` are substituted before `bash -n` |
| `llm.ChatMessage(role=..., content=...)` "has unknown arguments" | Pydantic models report an empty `inspect.signature` | Field names come from `model_fields` instead |
| `curl https://tavusapi.com/v2/pals` "is a dead link" | The API answers 401 without a key | 401 and 403 count as reachable |
| `@server.rtc_session(...)` with a `# ...` body "is invalid" | It's a deliberate excerpt | If a mechanical repair parses, it's a `note`, not a `fail` |

The [builder page](https://docs.livekit.io/agents/start/builder.md) still shows up as a JSON parse failure. It's a schema illustration with `...` placeholders, not a sample meant to parse, so I left it out of the findings. Deciding what's a bug in cases like that is why the skill tells the agent to confirm every failure before reporting it.

## What it checks

| Language | Checks |
|---|---|
| Python | Syntax, using the target interpreter. Every import, run in the target environment. Every attribute chain rooted at an imported name, such as `ai_coustics.EnhancerModel.QUAIL_VF_S`. Keyword arguments passed to imported callables. Optionally (`--run`), executes the block. |
| Shell (`shell`, `bash`, `console`, and `text` blocks that start with a known CLI) | `bash -n` syntax. With `--network`: `git clone` targets, and package names for pip/uv (PyPI), npm/pnpm/yarn (npm), and Homebrew, plus curl/wget URLs. Unquoted `pkg[extra]` that breaks zsh. Program output tagged as shell. |
| JSON, TOML | Parses them |
| JavaScript | `node --check`, if node is installed |
| TypeScript, others | Reported as skipped |

Nothing is executed unless you pass `--run`. Network checks are read-only lookups.

## Quick start

```bash
# An environment with the SDK the docs describe
uv venv .venv-docs --python 3.12
uv pip install --python .venv-docs/bin/python 'livekit-agents[mcp]' livekit-plugins-ai-coustics

# One page
python3 scripts/test_code_blocks.py https://docs.livekit.io/agents/start/voice-ai.md \
  --python .venv-docs/bin/python --network

# A whole section, problems only
python3 scripts/test_code_blocks.py https://docs.livekit.io/agents/llms.txt --index \
  --python .venv-docs/bin/python --network --only-problems > report.md
```

Example output:

```
| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 4 | 77 | text | Install the LiveKit CLI / From Source | FAIL | fail git clone: `github.com/livekit/livekit-cli` is not a reachable repository ... |
```

The exit code is 1 when any block fails, so the script can gate a docs CI job. A natural next step is running it on changed pages in a docs pull request.

## Using it as a skill

Copy this folder into your agent's skills directory, for example `~/.claude/skills/docs-code-tester/` for Claude Code. Then ask something like "test the code samples on this docs page". [`SKILL.md`](SKILL.md) walks the agent through setting up the environment, running the script, triaging statuses, verifying each failure, and writing the report.

[`tests/fixture.md`](tests/fixture.md) contains one block for each kind of problem the script should catch, or should *not* flag. Run the script on it after changing a heuristic:

```bash
python3 scripts/test_code_blocks.py tests/fixture.md --python .venv-docs/bin/python --network
```

## Limits

- Calls on instances (`session.start(...)`) can't be resolved statically. Only names imported in the block are checked.
- Keyword checks are skipped for callables that take `**kwargs`.
- No TypeScript checking yet. That's the obvious next addition, since LiveKit documents Python and Node.js side by side (417 TypeScript blocks in this sweep).
