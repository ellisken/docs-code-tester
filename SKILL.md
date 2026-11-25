---
name: docs-code-tester
description: Test the code samples in Markdown documentation. Extracts fenced code blocks from a docs page (local file or URL, or every page in an llms.txt index), checks them against the real SDK and package registries, and reports which samples fail and why. Use when asked to verify, audit, or test docs code samples, check a docs page for broken examples, find API drift between docs and an SDK, or review a docs PR's code blocks.
---

# Docs code tester

Docs code samples break quietly: an SDK renames a class, a package moves, an install
command picks up a typo. This skill finds those breaks by checking each sample against
the installed SDK, then has you confirm each failure before reporting it.

The script is `scripts/test_code_blocks.py` (standard library only, Python 3.9+).

## 1. Set up an environment with the documented packages

Import checks are only as good as the environment they run in. Create a virtualenv with
the SDK version the docs target, plus the extras the pages use. For LiveKit Agents:

```bash
uv venv .venv-docs --python 3.12
uv pip install --python .venv-docs/bin/python 'livekit-agents[mcp]' livekit-plugins-ai-coustics
```

Say which versions you installed in your report. A finding means "fails against version X".

## 2. Run the script

```bash
# One page
python3 scripts/test_code_blocks.py https://docs.livekit.io/agents/start/voice-ai.md \
  --python .venv-docs/bin/python --network

# A whole docs section, problems only
python3 scripts/test_code_blocks.py https://docs.livekit.io/agents/llms.txt --index \
  --python .venv-docs/bin/python --network --only-problems > report.md
```

Flags:

- `--python`: the interpreter whose environment has the SDK. Syntax is parsed by this interpreter too.
- `--network`: check `git clone` targets, PyPI/npm/Homebrew package names, and curl/wget URLs.
- `--index`: treat each argument as an `llms.txt` index and test every linked `.md` page. `--limit N` caps it.
- `--run`: also execute complete Python blocks (60s timeout). Only use this on docs you trust, in a sandbox.
- `--format json`: machine-readable output for further triage.

The exit code is 1 if any block has status `fail`.

## 3. Read the statuses

| Status | Meaning | What to do |
|---|---|---|
| `fail` | Syntax error, `cannot import name`, missing attribute, unknown keyword argument, unreachable repo, unknown package, invalid JSON/TOML | Verify by hand (step 4) |
| `env` | A module isn't installed (often an optional plugin) | Install it and rerun, or ignore it if the page is about a plugin you're not testing |
| `note` | Works with caveats: a deliberate fragment, `<placeholder>` values, shell commands in a `text` fence, output tagged as `shell`, unquoted `pkg[extra]` that zsh rejects | Style findings. Report the ones a reader would trip over |
| `skip` | No checker for this language, or the CLI isn't installed | Not a finding |
| `pass` | All checks passed | |

## 4. Verify every failure before reporting it

The script is a triage tool, not an oracle. For each `fail`:

1. Re-read the block in context. Is it a deliberate fragment the repair heuristics missed?
2. Reproduce it yourself in the same interpreter. For example, run
   `python -c "from livekit.agents import X"` or construct the object with the documented arguments.
3. Check whether the SDK's latest release or `main` branch has the name. Docs are
   sometimes written ahead of a release. If so, the finding is "docs are ahead of the
   release" rather than "wrong".
4. Find the right replacement (search the package source for a similar name) so the
   report includes a fix, not just a complaint.

Drop anything you can't reproduce. A false positive costs a docs team more time than a missed bug.

## 5. Report

For each confirmed finding, give the page URL and block line, what the sample says, what
actually happens (exact error), the suggested fix, and the SDK version tested. Group
style notes separately from breakages. Include the totals: pages, blocks, and blocks
checked versus skipped. That way readers know what "no failures" covered.

## Limits

- TypeScript and other non-Python languages are only reported as skipped. JavaScript gets `node --check` when node is installed.
- Calls on instances (`session.start(...)`) can't be resolved statically, so only imported names and attribute chains from them are checked.
- Keyword checks are skipped for callables that accept `**kwargs`.
