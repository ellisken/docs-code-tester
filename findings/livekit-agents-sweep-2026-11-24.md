Raw output of the 2026-11-24 sweep (problems only), run against livekit-agents 1.8.13 with the `mcp` extra and livekit-plugins-ai-coustics 0.3.6 on Python 3.14. `env` rows are plugins that weren't installed. They aren't docs bugs. See the README for the triaged findings.

# Code sample report

Blocks by worst status: 8 fail, 218 env, 30 note, 891 skip, 446 pass

## https://docs.livekit.io/agents.md

No problems found in 0 blocks.

## https://docs.livekit.io/agents/start/voice-ai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 4 | 77 | text | Install the LiveKit CLI / From Source | FAIL | **note** fence: shell commands in a `text` fence (no shell highlighting; tools can't tell it's runnable)<br>**fail** git clone: `github.com/livekit/livekit-cli` is not a reachable repository: fatal: 'github.com/livekit/livekit-cli' does not appear to be a git repository |

## https://docs.livekit.io/agents/start/builder.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 1 | 156 | json | Data collection mode results | FAIL | **fail** json: Expecting property name enclosed in double quotes: line 24 column 9 (char 725) |

## https://docs.livekit.io/testing/agent-console.md

No problems found in 0 blocks.

## https://docs.livekit.io/agents/start/embed.md

No problems found in 3 blocks.

## https://docs.livekit.io/agents/start/prompting.md

No problems found in 13 blocks.

## https://docs.livekit.io/agents/multimodality.md

No problems found in 0 blocks.

## https://docs.livekit.io/agents/multimodality/audio.md

No problems found in 27 blocks.

## https://docs.livekit.io/agents/multimodality/audio/customization.md

No problems found in 16 blocks.

## https://docs.livekit.io/agents/multimodality/audio/background-audio.md

No problems found in 15 blocks.

## https://docs.livekit.io/agents/multimodality/audio/wakeword.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 14 | 186 | python | Train via the Python API | ENV | **env** import: `from livekit.wakeword import WakeWordConfig` -> ModuleNotFoundError: No module named 'livekit.wakeword'<br>**env** import: `from livekit.wakeword import load_config` -> ModuleNotFoundError: No module named 'livekit.wakeword'<br>**env** import: `from livekit.wakeword import run_generate` -> ModuleNotFoundError: No module named 'livekit.wakeword'<br>**env** import: `from livekit.wakeword import run_augment` -> ModuleNotFoundError: No module named 'livekit.wakeword'<br>**env** import: `from livekit.wakeword import run_extraction` -> ModuleNotFoundError: No module named 'livekit.wakeword'<br>**env** import: `from livekit.wakeword import run_train` -> ModuleNotFoundError: No module named 'livekit.wakeword'<br>**env** import: `from livekit.wakeword import run_export` -> ModuleNotFoundError: No module named 'livekit.wakeword'<br>**env** import: `from livekit.wakeword import run_eval` -> ModuleNotFoundError: No module named 'livekit.wakeword' |
| 19 | 276 | python | Select a client SDK / Python | ENV | **env** import: `from livekit.wakeword import WakeWordModel` -> ModuleNotFoundError: No module named 'livekit.wakeword' |
| 20 | 289 | python | Select a client SDK / Python | ENV | **env** import: `from livekit.wakeword import WakeWordModel` -> ModuleNotFoundError: No module named 'livekit.wakeword'<br>**env** import: `from livekit.wakeword import WakeWordListener` -> ModuleNotFoundError: No module named 'livekit.wakeword' |

## https://docs.livekit.io/agents/multimodality/text.md

No problems found in 27 blocks.

## https://docs.livekit.io/agents/multimodality/instructions.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 9 | 176 | python | Customize built-in tasks | FAIL | **fail** import: `from livekit.agents.beta.workflows import InstructionParts` -> ImportError: cannot import name 'InstructionParts' from 'livekit.agents.beta.workflows' |

## https://docs.livekit.io/agents/multimodality/vision.md

No problems found in 0 blocks.

## https://docs.livekit.io/agents/multimodality/vision/images.md

No problems found in 16 blocks.

## https://docs.livekit.io/agents/multimodality/vision/video.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 8 | 281 | python | Adding an avatar to your agent / Required imports | ENV | **env** import: `from livekit.plugins import anam` -> ImportError: cannot import name 'anam' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/logic.md

No problems found in 0 blocks.

## https://docs.livekit.io/agents/logic/sessions.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 6 | 283 | python | Handling missing transcripts / Python | ENV | **env** import: `from livekit.plugins import silero` -> ImportError: cannot import name 'silero' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/logic/chat-context.md

No problems found in 22 blocks.

## https://docs.livekit.io/agents/logic/tasks.md

No problems found in 32 blocks.

## https://docs.livekit.io/agents/logic/workflows.md

No problems found in 0 blocks.

## https://docs.livekit.io/agents/logic/patterns.md

No problems found in 0 blocks.

## https://docs.livekit.io/agents/logic/patterns/supervisor.md

No problems found in 2 blocks.

## https://docs.livekit.io/agents/logic/patterns/subagent-delegation.md

No problems found in 7 blocks.

## https://docs.livekit.io/agents/logic/tools.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 1 | 41 | python | Provider tools / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/logic/tools/definition.md

No problems found in 37 blocks.

## https://docs.livekit.io/agents/logic/tools/toolsets.md

No problems found in 6 blocks.

## https://docs.livekit.io/agents/logic/tools/async.md

No problems found in 16 blocks.

## https://docs.livekit.io/agents/logic/tools/mcp.md

No problems found in 24 blocks.

## https://docs.livekit.io/agents/logic/tools/forwarding.md

No problems found in 3 blocks.

## https://docs.livekit.io/agents/logic/tools/design.md

No problems found in 18 blocks.

## https://docs.livekit.io/agents/logic/nodes.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 27 | 739 | python | Speeding up output audio / Python | ENV | **env** import: `import librosa` -> ModuleNotFoundError: No module named 'librosa' |
| 29 | 894 | python | Realtime audio output node / Python | FAIL | **fail** import: `from livekit.agents import rtc` -> ImportError: cannot import name 'rtc' from 'livekit.agents' |

## https://docs.livekit.io/agents/logic/turns.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 111 | python | Interruption in realtime mode / Python | ENV | **env** import: `from livekit.plugins.openai import realtime` -> ModuleNotFoundError: No module named 'livekit.plugins.openai' |
| 5 | 162 | python | Client-side turn-taking with realtime models / Python | ENV | **env** import: `from livekit.plugins import silero` -> ImportError: cannot import name 'silero' from 'livekit.plugins' (unknown location)<br>**env** import: `from livekit.plugins.openai import realtime` -> ModuleNotFoundError: No module named 'livekit.plugins.openai' |

## https://docs.livekit.io/agents/logic/turns/turn-detector.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 11 | 227 | python | Realtime model usage / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 15 | 369 | python | Usage / Python | ENV | **env** import: `from livekit.plugins.turn_detector.multilingual import MultilingualModel` -> ModuleNotFoundError: No module named 'livekit.plugins.turn_detector' |
| 19 | 476 | python | Realtime model usage / Python | ENV | **env** import: `from livekit.plugins.turn_detector.multilingual import MultilingualModel` -> ModuleNotFoundError: No module named 'livekit.plugins.turn_detector'<br>**env** import: `from livekit.plugins import deepgram` -> ImportError: cannot import name 'deepgram' from 'livekit.plugins' (unknown location)<br>**env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location)<br>**env** import: `from livekit.plugins import silero` -> ImportError: cannot import name 'silero' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/logic/turns/adaptive-interruption-handling.md

No problems found in 7 blocks.

## https://docs.livekit.io/agents/logic/turns/vad.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 55 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import silero` -> ImportError: cannot import name 'silero' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/logic/turns/tuning.md

No problems found in 2 blocks.

## https://docs.livekit.io/agents/logic/agents-handoffs.md

No problems found in 26 blocks.

## https://docs.livekit.io/agents/logic/external-data.md

No problems found in 10 blocks.

## https://docs.livekit.io/agents/logic/fallback-strategies.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 120 | python | Agent Fallback Adapter / Python | ENV | **note** fragment: doesn't parse as pasted (line 14: positional argument follows keyword argument); uses `...` in place of other arguments<br>**env** import: `from livekit.plugins import assemblyai` -> ImportError: cannot import name 'assemblyai' from 'livekit.plugins' (unknown location)<br>**env** import: `from livekit.plugins import cartesia` -> ImportError: cannot import name 'cartesia' from 'livekit.plugins' (unknown location)<br>**env** import: `from livekit.plugins import deepgram` -> ImportError: cannot import name 'deepgram' from 'livekit.plugins' (unknown location)<br>**env** import: `from livekit.plugins import inworld` -> ImportError: cannot import name 'inworld' from 'livekit.plugins' (unknown location)<br>**env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 6 | 204 | python | Realtime Model Fallback Adapter | ENV | **env** import: `from livekit.plugins import google` -> ImportError: cannot import name 'google' from 'livekit.plugins' (unknown location)<br>**env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/prebuilt/tasks.md

No problems found in 0 blocks.

## https://docs.livekit.io/agents/prebuilt/tasks/get-name.md

No problems found in 2 blocks.

## https://docs.livekit.io/agents/prebuilt/tasks/get-email.md

No problems found in 2 blocks.

## https://docs.livekit.io/agents/prebuilt/tasks/get-address.md

No problems found in 1 blocks.

## https://docs.livekit.io/agents/prebuilt/tasks/get-dob.md

No problems found in 2 blocks.

## https://docs.livekit.io/agents/prebuilt/tasks/get-phone-number.md

No problems found in 1 blocks.

## https://docs.livekit.io/agents/prebuilt/tasks/get-dtmf.md

No problems found in 1 blocks.

## https://docs.livekit.io/agents/prebuilt/tasks/warm-transfer.md

No problems found in 2 blocks.

## https://docs.livekit.io/agents/prebuilt/tools.md

No problems found in 0 blocks.

## https://docs.livekit.io/agents/prebuilt/tools/end-call-tool.md

No problems found in 4 blocks.

## https://docs.livekit.io/agents/prebuilt/tools/send-dtmf-events.md

No problems found in 1 blocks.

## https://docs.livekit.io/agents/server.md

No problems found in 0 blocks.

## https://docs.livekit.io/agents/server/startup-modes.md

No problems found in 16 blocks.

## https://docs.livekit.io/agents/server/lifecycle.md

No problems found in 0 blocks.

## https://docs.livekit.io/agents/server/agent-dispatch.md

No problems found in 17 blocks.

## https://docs.livekit.io/agents/server/job.md

No problems found in 16 blocks.

## https://docs.livekit.io/agents/server/options.md

No problems found in 25 blocks.

## https://docs.livekit.io/agents/models.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 51 | python | OpenAI API compatibility / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 7 | 138 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location)<br>**env** import: `from livekit.plugins import cartesia` -> ImportError: cannot import name 'cartesia' from 'livekit.plugins' (unknown location)<br>**env** import: `from livekit.plugins import assemblyai` -> ImportError: cannot import name 'assemblyai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/pipelines.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 5 | 153 | python | Turn-based example / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/inference.md

No problems found in 6 blocks.

## https://docs.livekit.io/agents/models/llm.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 203 | python | Standalone usage | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/livekit.md

No problems found in 4 blocks.

## https://docs.livekit.io/agents/models/llm/deepseek.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 8 | 172 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/gemini.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 7 | 191 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import google` -> ImportError: cannot import name 'google' from 'livekit.plugins' (unknown location) |
| 9 | 270 | python | Configure thinking / Python | ENV | **env** import: `from livekit.plugins import google` -> ImportError: cannot import name 'google' from 'livekit.plugins' (unknown location) |
| 11 | 331 | python | Context caching / Python | ENV | **env** import: `from google import genai` -> ImportError: cannot import name 'genai' from 'google' (unknown location)<br>**env** import: `from google.genai import types` -> ModuleNotFoundError: No module named 'google.genai'<br>**env** import: `from livekit.plugins import google` -> ImportError: cannot import name 'google' from 'livekit.plugins' (unknown location) |
| 13 | 417 | python | Provider tools / Python | ENV | **env** import: `from livekit.plugins import google` -> ImportError: cannot import name 'google' from 'livekit.plugins' (unknown location) |
| 15 | 447 | python | Provider tools / Python | ENV | **env** import: `from livekit.plugins import google` -> ImportError: cannot import name 'google' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/kimi.md

No problems found in 4 blocks.

## https://docs.livekit.io/agents/models/llm/meta.md

No problems found in 2 blocks.

## https://docs.livekit.io/agents/models/llm/openai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 7 | 203 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 9 | 251 | python | Responses API (Recommended) / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 11 | 293 | python | Chat Completions API / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 14 | 406 | python | Provider tools / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/spacexai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 8 | 180 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import xai` -> ImportError: cannot import name 'xai' from 'livekit.plugins' (unknown location) |
| 10 | 241 | python | Provider tools | ENV | **env** import: `from livekit.plugins import xai` -> ImportError: cannot import name 'xai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/anthropic.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 49 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import anthropic` -> ImportError: cannot import name 'anthropic' from 'livekit.plugins' (unknown location) |
| 5 | 123 | python | Provider tools | ENV | **env** import: `from livekit.plugins import anthropic` -> ImportError: cannot import name 'anthropic' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/aws.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 40 | python | Usage | ENV | **env** import: `from livekit.plugins import aws` -> ImportError: cannot import name 'aws' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/baseten.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 53 | python | Usage | ENV | **env** import: `from livekit.plugins import baseten` -> ImportError: cannot import name 'baseten' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/cerebras.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 4 | 52 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import cerebras` -> ImportError: cannot import name 'cerebras' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/fireworks.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 4 | 48 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/groq.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 53 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import groq` -> ImportError: cannot import name 'groq' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/langchain.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 30 | python | Usage | ENV | **env** import: `from langchain.chat_models import init_chat_model` -> ModuleNotFoundError: No module named 'langchain'<br>**env** import: `from langchain_core.messages import BaseMessage` -> ModuleNotFoundError: No module named 'langchain_core'<br>**env** import: `from langgraph.graph import START` -> ModuleNotFoundError: No module named 'langgraph'<br>**env** import: `from langgraph.graph import StateGraph` -> ModuleNotFoundError: No module named 'langgraph'<br>**env** import: `from langgraph.graph.message import add_messages` -> ModuleNotFoundError: No module named 'langgraph'<br>**env** import: `from livekit.plugins import langchain` -> ImportError: cannot import name 'langchain' from 'livekit.plugins' (unknown location) |
| 4 | 104 | python | Stream custom data | ENV | **env** import: `from langchain_core.messages import AIMessage` -> ModuleNotFoundError: No module named 'langchain_core'<br>**env** import: `from langgraph.config import get_stream_writer` -> ModuleNotFoundError: No module named 'langgraph' |
| 6 | 146 | python | Complete example | ENV | **env** import: `from langchain.chat_models import init_chat_model` -> ModuleNotFoundError: No module named 'langchain'<br>**env** import: `from langchain_core.messages import BaseMessage` -> ModuleNotFoundError: No module named 'langchain_core'<br>**env** import: `from langgraph.graph import START` -> ModuleNotFoundError: No module named 'langgraph'<br>**env** import: `from langgraph.graph import StateGraph` -> ModuleNotFoundError: No module named 'langgraph'<br>**env** import: `from langgraph.graph.message import add_messages` -> ModuleNotFoundError: No module named 'langgraph'<br>**env** import: `from livekit.plugins import langchain` -> ImportError: cannot import name 'langchain' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/letta.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/mistralai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 49 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import mistralai` -> ImportError: cannot import name 'mistralai' from 'livekit.plugins' (unknown location) |
| 5 | 126 | python | Provider tools | ENV | **env** import: `from livekit.plugins import mistralai` -> ImportError: cannot import name 'mistralai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/ollama.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 28 | python | Usage | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/azure-openai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 61 | python | Usage | ENV | **env** import: `from livekit.plugins import azure` -> ImportError: cannot import name 'azure' from 'livekit.plugins' (unknown location) |
| 5 | 118 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/openrouter.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 34 | python | Authentication | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 3 | 77 | python | Examples | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 4 | 92 | python | Examples | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 5 | 108 | python | Examples | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 6 | 125 | python | Examples | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/ovhcloud.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 49 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/perplexity.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 4 | 52 | python | Chat completions / Python | ENV | **env** import: `from livekit.plugins import perplexity` -> ImportError: cannot import name 'perplexity' from 'livekit.plugins' (unknown location) |
| 6 | 110 | python | Agent API | ENV | **env** import: `from livekit.plugins import perplexity` -> ImportError: cannot import name 'perplexity' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/sarvam.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 38 | python | Usage | ENV | **env** import: `from livekit.plugins import sarvam` -> ImportError: cannot import name 'sarvam' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/telnyx.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 4 | 48 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/together.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 4 | 48 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/llm/openai-compatible-llms.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 63 | python | Using a custom endpoint / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 7 | 547 | python | Standalone usage / agent.py | ENV | **env** import: `from livekit.plugins import deepgram` -> ImportError: cannot import name 'deepgram' from 'livekit.plugins' (unknown location) |
| 8 | 618 | python | VAD and StreamAdapter | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/assemblyai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 11 | 301 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import assemblyai` -> ImportError: cannot import name 'assemblyai' from 'livekit.plugins' (unknown location) |
| 22 | 650 | python | Agent context / Python | ENV | **env** import: `from livekit.plugins import assemblyai` -> ImportError: cannot import name 'assemblyai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/cartesia.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 6 | 140 | python | Usage | ENV | **env** import: `from livekit.plugins import cartesia` -> ImportError: cannot import name 'cartesia' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/deepgram.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 8 | 227 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import deepgram` -> ImportError: cannot import name 'deepgram' from 'livekit.plugins' (unknown location) |
| 10 | 289 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import deepgram` -> ImportError: cannot import name 'deepgram' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/gemini.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 7 | 177 | python | Usage | ENV | **env** import: `from livekit.plugins import google` -> ImportError: cannot import name 'google' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/inworld.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 51 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import inworld` -> ImportError: cannot import name 'inworld' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/meta.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 4 | 56 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import meta` -> ImportError: cannot import name 'meta' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/openai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 5 | 119 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/spacexai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 7 | 153 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import xai` -> ImportError: cannot import name 'xai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/speechmatics.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 5 | 165 | python | Usage | ENV | **env** import: `from livekit.plugins import speechmatics` -> ImportError: cannot import name 'speechmatics' from 'livekit.plugins' (unknown location) |
| 6 | 192 | python | Turn detection | ENV | **env** import: `from livekit.plugins import speechmatics` -> ImportError: cannot import name 'speechmatics' from 'livekit.plugins' (unknown location) |
| 7 | 264 | python | Keyterms | ENV | **env** import: `from livekit.plugins import speechmatics` -> ImportError: cannot import name 'speechmatics' from 'livekit.plugins' (unknown location)<br>**env** import: `from livekit.plugins.speechmatics import AdditionalVocabEntry` -> ModuleNotFoundError: No module named 'livekit.plugins.speechmatics' |

## https://docs.livekit.io/agents/models/stt/aws.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 43 | python | Usage | ENV | **env** import: `from livekit.plugins import aws` -> ImportError: cannot import name 'aws' from 'livekit.plugins' (unknown location) |
| 4 | 67 | python | Single-language auto-detection | ENV | **env** import: `from livekit.plugins import aws` -> ImportError: cannot import name 'aws' from 'livekit.plugins' (unknown location) |
| 5 | 84 | python | Mid-stream language switching | ENV | **env** import: `from livekit.plugins import aws` -> ImportError: cannot import name 'aws' from 'livekit.plugins' (unknown location) |
| 6 | 101 | python | Multilingual turn detection | ENV | **env** import: `from livekit.plugins import aws` -> ImportError: cannot import name 'aws' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/azure.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 43 | python | Usage | ENV | **env** import: `from livekit.plugins import azure` -> ImportError: cannot import name 'azure' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/azure-openai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 45 | python | Usage | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/baseten.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 4 | 61 | python | Usage | ENV | **env** import: `from livekit.plugins import baseten` -> ImportError: cannot import name 'baseten' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/clova.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 40 | python | Usage | ENV | **env** import: `from livekit.plugins import clova` -> ImportError: cannot import name 'clova' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/elevenlabs.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 53 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import elevenlabs` -> ImportError: cannot import name 'elevenlabs' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/fal.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import fal` -> ImportError: cannot import name 'fal' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/gladia.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Initialization | ENV | **env** import: `from livekit.plugins import gladia` -> ImportError: cannot import name 'gladia' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/gnani.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 41 | python | Usage | ENV | **env** import: `from livekit.plugins import gnani` -> ImportError: cannot import name 'gnani' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/google.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 38 | python | Usage | ENV | **env** import: `from livekit.plugins import google` -> ImportError: cannot import name 'google' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/gradium.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 41 | python | Usage | ENV | **env** import: `from livekit.plugins import gradium` -> ImportError: cannot import name 'gradium' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/groq.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 51 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import groq` -> ImportError: cannot import name 'groq' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/microsoft-ai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 44 | python | Usage | ENV | **env** import: `from livekit.plugins import microsoft_ai` -> ImportError: cannot import name 'microsoft_ai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/mistralai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 49 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import mistralai` -> ImportError: cannot import name 'mistralai' from 'livekit.plugins' (unknown location) |
| 5 | 116 | python | Turn detection | ENV | **env** import: `from livekit.plugins import mistralai` -> ImportError: cannot import name 'mistralai' from 'livekit.plugins' (unknown location) |
| 6 | 150 | python | Speaker diarization | ENV | **env** import: `from livekit.plugins import mistralai` -> ImportError: cannot import name 'mistralai' from 'livekit.plugins' (unknown location)<br>**env** import: `from livekit.plugins import silero` -> ImportError: cannot import name 'silero' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/nabrah.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 43 | python | Usage | ENV | **env** import: `from livekit.plugins import nabrah` -> ImportError: cannot import name 'nabrah' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/nvidia.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 37 | python | Usage | ENV | **env** import: `from livekit.plugins import nvidia` -> ImportError: cannot import name 'nvidia' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/ovhcloud.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 49 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/sarvam.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 4 | 65 | python | Usage | ENV | **env** import: `from livekit.plugins import sarvam` -> ImportError: cannot import name 'sarvam' from 'livekit.plugins' (unknown location) |
| 5 | 117 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import sarvam` -> ImportError: cannot import name 'sarvam' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/simplismart.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import simplismart` -> ImportError: cannot import name 'simplismart' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/slng.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 40 | python | Usage | ENV | **env** import: `from livekit.plugins import slng` -> ImportError: cannot import name 'slng' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/smallestai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import smallestai` -> ImportError: cannot import name 'smallestai' from 'livekit.plugins' (unknown location) |
| 3 | 66 | python | Speaker diarization | ENV | **env** import: `from livekit.plugins import smallestai` -> ImportError: cannot import name 'smallestai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/soniox.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 51 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import soniox` -> ImportError: cannot import name 'soniox' from 'livekit.plugins' (unknown location) |
| 5 | 92 | python | Speaker diarization / Python | ENV | **env** import: `from livekit.plugins import soniox` -> ImportError: cannot import name 'soniox' from 'livekit.plugins' (unknown location) |
| 7 | 139 | python | One-way translation / Python | ENV | **env** import: `from livekit.plugins import soniox` -> ImportError: cannot import name 'soniox' from 'livekit.plugins' (unknown location) |
| 9 | 184 | python | Two-way translation / Python | ENV | **env** import: `from livekit.plugins import soniox` -> ImportError: cannot import name 'soniox' from 'livekit.plugins' (unknown location) |
| 12 | 258 | python | Endpoint detection / Python | ENV | **env** import: `from livekit.plugins import soniox` -> ImportError: cannot import name 'soniox' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/spitch.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import spitch` -> ImportError: cannot import name 'spitch' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/stt/keyterms.md

No problems found in 8 blocks.

## https://docs.livekit.io/agents/models/stt/diarization.md

No problems found in 5 blocks.

## https://docs.livekit.io/agents/models/tts.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 5 | 348 | python | Standalone TTS / agent.py | ENV | **env** import: `from livekit.plugins import cartesia` -> ImportError: cannot import name 'cartesia' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/assemblyai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 7 | 161 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import assemblyai` -> ImportError: cannot import name 'assemblyai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/cartesia.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 7 | 203 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import cartesia` -> ImportError: cannot import name 'cartesia' from 'livekit.plugins' (unknown location) |
| 9 | 263 | python | Connection pooling / Python | ENV | **env** import: `from livekit.plugins import cartesia` -> ImportError: cannot import name 'cartesia' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/deepgram.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 7 | 176 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import deepgram` -> ImportError: cannot import name 'deepgram' from 'livekit.plugins' (unknown location) |
| 9 | 222 | python | Usage | ENV | **env** import: `from livekit.plugins import deepgram` -> ImportError: cannot import name 'deepgram' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/fishaudio.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 7 | 203 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import fishaudio` -> ImportError: cannot import name 'fishaudio' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/gemini.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 52 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import google` -> ImportError: cannot import name 'google' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/gradium.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 7 | 179 | python | Usage | ENV | **env** import: `from livekit.plugins import gradium` -> ImportError: cannot import name 'gradium' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/inworld.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 7 | 183 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import inworld` -> ImportError: cannot import name 'inworld' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/rime.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 7 | 182 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import rime` -> ImportError: cannot import name 'rime' from 'livekit.plugins' (unknown location) |
| 9 | 219 | python | WebSocket streaming / Python | ENV | **env** import: `from livekit.plugins import rime` -> ImportError: cannot import name 'rime' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/spacexai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 6 | 169 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import xai` -> ImportError: cannot import name 'xai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/asyncai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 40 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import asyncai` -> ImportError: cannot import name 'asyncai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/aws.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 43 | python | Usage | ENV | **env** import: `from livekit.plugins import aws` -> ImportError: cannot import name 'aws' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/azure.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 43 | python | Usage | ENV | **env** import: `from livekit.plugins import azure` -> ImportError: cannot import name 'azure' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/azure-openai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 45 | python | Usage | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/baseten.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 63 | python | Usage | ENV | **env** import: `from livekit.plugins import baseten` -> ImportError: cannot import name 'baseten' from 'livekit.plugins' (unknown location) |
| 5 | 88 | python | Qwen3-TTS voices | ENV | **env** import: `from livekit.plugins.baseten import register_voice` -> ModuleNotFoundError: No module named 'livekit.plugins.baseten' |

## https://docs.livekit.io/agents/models/tts/bland.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import bland` -> ImportError: cannot import name 'bland' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/cambai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 40 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import cambai` -> ImportError: cannot import name 'cambai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/elevenlabs.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 53 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import elevenlabs` -> ImportError: cannot import name 'elevenlabs' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/gnani.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 41 | python | Usage | ENV | **env** import: `from livekit.plugins import gnani` -> ImportError: cannot import name 'gnani' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/google.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 38 | python | Usage | ENV | **env** import: `from livekit.plugins import google` -> ImportError: cannot import name 'google' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/groq.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import groq` -> ImportError: cannot import name 'groq' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/hume.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import hume` -> ImportError: cannot import name 'hume' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/kokoro.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 30 | python | Usage | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/lmnt.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import lmnt` -> ImportError: cannot import name 'lmnt' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/microsoft-ai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 40 | python | Usage | ENV | **env** import: `from livekit.plugins import microsoft_ai` -> ImportError: cannot import name 'microsoft_ai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/minimax.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import minimax` -> ImportError: cannot import name 'minimax' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/mistralai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 49 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import mistralai` -> ImportError: cannot import name 'mistralai' from 'livekit.plugins' (unknown location) |
| 5 | 117 | python | Realtime streaming | ENV | **env** import: `from livekit.plugins import mistralai` -> ImportError: cannot import name 'mistralai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/murf.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import murf` -> ImportError: cannot import name 'murf' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/neuphonic.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import neuphonic` -> ImportError: cannot import name 'neuphonic' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/nvidia.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 37 | python | Usage | ENV | **env** import: `from livekit.plugins import nvidia` -> ImportError: cannot import name 'nvidia' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/openai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 51 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/resemble.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import resemble` -> ImportError: cannot import name 'resemble' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/respeecher.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import respeecher` -> ImportError: cannot import name 'respeecher' from 'livekit.plugins' (unknown location) |
| 3 | 62 | python | Voice discovery | ENV | **env** import: `from livekit.plugins import respeecher` -> ImportError: cannot import name 'respeecher' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/sarvam.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 4 | 64 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import sarvam` -> ImportError: cannot import name 'sarvam' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/simplismart.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 44 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import simplismart` -> ImportError: cannot import name 'simplismart' from 'livekit.plugins' (unknown location) |
| 3 | 87 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import simplismart` -> ImportError: cannot import name 'simplismart' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/slng.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 40 | python | Usage | ENV | **env** import: `from livekit.plugins import slng` -> ImportError: cannot import name 'slng' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/smallestai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import smallestai` -> ImportError: cannot import name 'smallestai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/soniox.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 49 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import soniox` -> ImportError: cannot import name 'soniox' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/speechify.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import speechify` -> ImportError: cannot import name 'speechify' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/speechmatics.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 40 | python | Usage | ENV | **env** import: `from livekit.plugins import speechmatics` -> ImportError: cannot import name 'speechmatics' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/spitch.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 36 | python | Usage | ENV | **env** import: `from livekit.plugins import spitch` -> ImportError: cannot import name 'spitch' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/vakyam.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 41 | python | Usage | ENV | **env** import: `from livekit.plugins import vakyam` -> ImportError: cannot import name 'vakyam' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/tts/custom-voices.md

No problems found in 6 blocks.

## https://docs.livekit.io/agents/models/tts/expressive.md

No problems found in 8 blocks.

## https://docs.livekit.io/agents/models/realtime.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 124 | python | Plugin usage / agent.py | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 9 | 238 | python | Access the duplex session / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/realtime/azure-openai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 6 | 128 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 8 | 198 | python | Server VAD / Python | ENV | **env** import: `from livekit.plugins.openai import realtime` -> ModuleNotFoundError: No module named 'livekit.plugins.openai' |

## https://docs.livekit.io/agents/models/realtime/gemini.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 7 | 143 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import google` -> ImportError: cannot import name 'google' from 'livekit.plugins' (unknown location) |
| 13 | 307 | python | Turn detection / Python | ENV | **env** import: `from google.genai import types` -> ModuleNotFoundError: No module named 'google.genai' |
| 16 | 406 | python | Video input / Required imports | ENV | **env** import: `from livekit.plugins import google` -> ImportError: cannot import name 'google' from 'livekit.plugins' (unknown location) |
| 17 | 432 | python | Usage with separate TTS / Python | ENV | **env** import: `from google.genai.types import Modality` -> ModuleNotFoundError: No module named 'google.genai' |

## https://docs.livekit.io/agents/models/realtime/gpt-live.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 7 | 179 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 9 | 265 | python | Voice and backend instructions / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 11 | 343 | python | Tools / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 13 | 419 | python | Client delegation / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/realtime/openai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 9 | 204 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 12 | 290 | python | Video input / Required imports | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |
| 17 | 402 | python | Semantic VAD / Plugin / agent.py | ENV | **env** import: `from livekit.plugins.openai import realtime` -> ModuleNotFoundError: No module named 'livekit.plugins.openai' |
| 21 | 501 | python | Server VAD / Plugin / agent.py | ENV | **env** import: `from livekit.plugins.openai import realtime` -> ModuleNotFoundError: No module named 'livekit.plugins.openai' |

## https://docs.livekit.io/agents/models/realtime/rime.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 77 | python | Usage | ENV | **env** import: `from livekit.plugins import rime` -> ImportError: cannot import name 'rime' from 'livekit.plugins' (unknown location)<br>**env** import: `from rimelabs_sdk.realtime import TurnDetection` -> ModuleNotFoundError: No module named 'rimelabs_sdk' |

## https://docs.livekit.io/agents/models/realtime/spacexai.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 7 | 143 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import xai` -> ImportError: cannot import name 'xai' from 'livekit.plugins' (unknown location) |
| 9 | 201 | python | Tools | ENV | **env** import: `from livekit.plugins import xai` -> ImportError: cannot import name 'xai' from 'livekit.plugins' (unknown location) |
| 12 | 291 | python | Turn detection / Plugin / agent.py | ENV | **env** import: `from livekit.plugins import xai` -> ImportError: cannot import name 'xai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/realtime/nova-sonic.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 40 | python | Usage | ENV | **env** import: `from livekit.plugins import aws` -> ImportError: cannot import name 'aws' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/realtime/personaplex.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 45 | python | Usage | ENV | **env** import: `from livekit.plugins import nvidia` -> ImportError: cannot import name 'nvidia' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/realtime/phonic.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 47 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import phonic` -> ImportError: cannot import name 'phonic' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/realtime/thunderphone.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 45 | python | Saved agent | ENV | **env** import: `from livekit.plugins import thunderphone` -> ImportError: cannot import name 'thunderphone' from 'livekit.plugins' (unknown location) |
| 4 | 59 | python | Inline session | ENV | **env** import: `from livekit.plugins import thunderphone` -> ImportError: cannot import name 'thunderphone' from 'livekit.plugins' (unknown location) |
| 5 | 102 | python | Call events | ENV | **env** import: `from livekit.plugins import thunderphone` -> ImportError: cannot import name 'thunderphone' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/realtime/ultravox.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 34 | python | Usage | ENV | **env** import: `from livekit.plugins import ultravox` -> ImportError: cannot import name 'ultravox' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/avatar.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 1 | 54 | python | Sample code | ENV | **env** import: `from livekit.plugins import anam` -> ImportError: cannot import name 'anam' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/avatar/plugins/anam.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 49 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import anam` -> ImportError: cannot import name 'anam' from 'livekit.plugins' (unknown location) |
| 5 | 133 | python | Director notes | ENV | **env** import: `from livekit.plugins import anam` -> ImportError: cannot import name 'anam' from 'livekit.plugins' (unknown location) |
| 6 | 162 | python | AI disclosure | ENV | **env** import: `from livekit.plugins import anam` -> ImportError: cannot import name 'anam' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/avatar/plugins/avatario.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 42 | python | Usage | ENV | **env** import: `from livekit.plugins import avatario` -> ImportError: cannot import name 'avatario' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/avatar/plugins/avatartalk.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 46 | python | Usage | ENV | **env** import: `from livekit.plugins import avatartalk` -> ImportError: cannot import name 'avatartalk' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/avatar/plugins/bey.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 49 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import bey` -> ImportError: cannot import name 'bey' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/avatar/plugins/bithuman.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 54 | python | Pass image directly | ENV | **env** import: `from PIL import Image` -> ModuleNotFoundError: No module named 'PIL'<br>**env** import: `from livekit.plugins import bithuman` -> ImportError: cannot import name 'bithuman' from 'livekit.plugins' (unknown location) |
| 3 | 78 | python | Usage | ENV | **env** import: `from livekit.plugins import bithuman` -> ImportError: cannot import name 'bithuman' from 'livekit.plugins' (unknown location) |
| 4 | 101 | python | Usage | ENV | **env** import: `from livekit.plugins import bithuman` -> ImportError: cannot import name 'bithuman' from 'livekit.plugins' (unknown location)<br>**env** import: `from PIL import Image` -> ModuleNotFoundError: No module named 'PIL' |

## https://docs.livekit.io/agents/models/avatar/plugins/did.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 49 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import did` -> ImportError: cannot import name 'did' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/avatar/plugins/keyframe.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 4 | 66 | python | Usage | ENV | **env** import: `from livekit.plugins import keyframe` -> ImportError: cannot import name 'keyframe' from 'livekit.plugins' (unknown location) |
| 5 | 145 | python | Expressive mode | ENV | **env** import: `from livekit.plugins import keyframe` -> ImportError: cannot import name 'keyframe' from 'livekit.plugins' (unknown location) |
| 6 | 170 | python | Other TTS | ENV | **env** import: `from livekit.plugins import keyframe` -> ImportError: cannot import name 'keyframe' from 'livekit.plugins' (unknown location) |
| 7 | 192 | python | ElevenLabs plugin | ENV | **env** import: `from livekit.plugins import elevenlabs` -> ImportError: cannot import name 'elevenlabs' from 'livekit.plugins' (unknown location)<br>**env** import: `from livekit.plugins import keyframe` -> ImportError: cannot import name 'keyframe' from 'livekit.plugins' (unknown location) |
| 9 | 231 | python | Set an expression directly | ENV | **env** import: `from livekit.plugins import keyframe` -> ImportError: cannot import name 'keyframe' from 'livekit.plugins' (unknown location)<br>**env** import: `from livekit.plugins.keyframe import Emotion` -> ModuleNotFoundError: No module named 'livekit.plugins.keyframe' |

## https://docs.livekit.io/agents/models/avatar/plugins/lemonslice.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 61 | python | Agent image / Python | ENV | **env** import: `from PIL import Image` -> ModuleNotFoundError: No module named 'PIL' |
| 5 | 102 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import lemonslice` -> ImportError: cannot import name 'lemonslice' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/avatar/plugins/liveavatar.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 44 | python | Usage | ENV | **env** import: `from livekit.plugins import liveavatar` -> ImportError: cannot import name 'liveavatar' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/avatar/plugins/protoface.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 53 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import protoface` -> ImportError: cannot import name 'protoface' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/avatar/plugins/runway.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 59 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import runway` -> ImportError: cannot import name 'runway' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/avatar/plugins/simli.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 38 | python | Usage | ENV | **env** import: `from livekit.plugins import simli` -> ImportError: cannot import name 'simli' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/avatar/plugins/spatius.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 54 | python | Usage | ENV | **env** import: `from livekit.plugins import spatius` -> ImportError: cannot import name 'spatius' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/avatar/plugins/synthesia.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 2 | 50 | python | Usage | ENV | **env** import: `from livekit.plugins import synthesia` -> ImportError: cannot import name 'synthesia' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/avatar/plugins/tavus.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 5 | 98 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import tavus` -> ImportError: cannot import name 'tavus' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/models/avatar/plugins/trugen.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 49 | python | Usage / Python | ENV | **env** import: `from livekit.plugins import trugen` -> ImportError: cannot import name 'trugen' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/integrations/openai.md

No problems found in 7 blocks.

## https://docs.livekit.io/agents/integrations/google.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 5 | 106 | text | LiveKit CLI / From Source | FAIL | **note** fence: shell commands in a `text` fence (no shell highlighting; tools can't tell it's runnable)<br>**fail** git clone: `github.com/livekit/livekit-cli` is not a reachable repository: fatal: 'github.com/livekit/livekit-cli' does not appear to be a git repository |
| 13 | 242 | python | Agent code / Gemini Live API / agent.py | ENV | **env** import: `from livekit.plugins import google` -> ImportError: cannot import name 'google' from 'livekit.plugins' (unknown location) |
| 14 | 298 | python | Agent code / STT-LLM-TTS pipeline / agent.py | ENV | **env** import: `from livekit.plugins import google` -> ImportError: cannot import name 'google' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/integrations/azure.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 5 | 83 | python | Azure OpenAI Realtime API / agent.py | ENV | **env** import: `from livekit.plugins import openai` -> ImportError: cannot import name 'openai' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/integrations/aws.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 48 | python | Getting started / agent.py | ENV | **env** import: `from livekit.plugins import aws` -> ImportError: cannot import name 'aws' from 'livekit.plugins' (unknown location) |
| 5 | 81 | python | Getting started / agent.py | ENV | **env** import: `from livekit.plugins import aws` -> ImportError: cannot import name 'aws' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/agents/integrations/spacexai.md

No problems found in 2 blocks.

## https://docs.livekit.io/agents/integrations/groq.md

No problems found in 2 blocks.

## https://docs.livekit.io/agents/integrations/cerebras.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 3 | 41 | python | Getting started / agent.py | ENV | **env** import: `from livekit.plugins import cerebras` -> ImportError: cannot import name 'cerebras' from 'livekit.plugins' (unknown location) |

## https://docs.livekit.io/reference/agents/turn-handling-options.md

No problems found in 18 blocks.

## https://docs.livekit.io/reference/agents/events.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 12 | 535 | python | Continue after an error / Python | FAIL | **fail** import: `from livekit.agents import multimodal` -> ImportError: cannot import name 'multimodal' from 'livekit.agents' |

## https://docs.livekit.io/reference/agents/agent-dispatch-service-api.md

No problems found in 4 blocks.

## https://docs.livekit.io/reference/developer-tools/livekit-cli.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 4 | 84 | text | Install the CLI / From Source | FAIL | **note** fence: shell commands in a `text` fence (no shell highlighting; tools can't tell it's runnable)<br>**fail** git clone: `github.com/livekit/livekit-cli` is not a reachable repository: fatal: 'github.com/livekit/livekit-cli' does not appear to be a git repository |

## https://docs.livekit.io/reference/agents/inference-llm-parameters.md

No problems found in 4 blocks.

## https://docs.livekit.io/testing.md

No problems found in 0 blocks.

## https://docs.livekit.io/testing/overview.md

No problems found in 0 blocks.

## https://docs.livekit.io/testing/agent-console.md

No problems found in 0 blocks.

## https://docs.livekit.io/testing/debugger.md

No problems found in 12 blocks.

## https://docs.livekit.io/testing/unit-tests.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 5 | 125 | python | Example test / Python | ENV | **env** import: `from agent import Assistant` -> ModuleNotFoundError: No module named 'agent' |
| 25 | 527 | python | Run a JudgeGroup in pytest | ENV | **env** import: `from agent import Assistant` -> ModuleNotFoundError: No module named 'agent' |

## https://docs.livekit.io/testing/simulations.md

No problems found in 22 blocks.

## https://docs.livekit.io/testing/simulations/write-a-scenario.md

No problems found in 6 blocks.

## https://docs.livekit.io/testing/simulations/scenario-group.md

No problems found in 3 blocks.

## https://docs.livekit.io/testing/simulations/derive-a-scenario.md

No problems found in 4 blocks.

## https://docs.livekit.io/testing/simulations/ci.md

No problems found in 6 blocks.

## https://docs.livekit.io/testing/simulations/dashboard.md

No problems found in 0 blocks.

## https://docs.livekit.io/testing/observability.md

No problems found in 0 blocks.

## https://docs.livekit.io/testing/observability/insights.md

No problems found in 1 blocks.

## https://docs.livekit.io/testing/observability/pii-redaction.md

No problems found in 0 blocks.

## https://docs.livekit.io/testing/observability/data-residency.md

No problems found in 0 blocks.

## https://docs.livekit.io/testing/observability/troubleshooting.md

No problems found in 1 blocks.

## https://docs.livekit.io/testing/observability/build.md

No problems found in 0 blocks.

## https://docs.livekit.io/testing/observability/tracing.md

No problems found in 5 blocks.

## https://docs.livekit.io/testing/observability/data.md

No problems found in 18 blocks.

## https://docs.livekit.io/testing/observability/recording.md

No problems found in 0 blocks.

## https://docs.livekit.io/reference/developer-tools/livekit-cli.md

| # | Line | Lang | Section | Status | Details |
|---|---|---|---|---|---|
| 4 | 84 | text | Install the CLI / From Source | FAIL | **note** fence: shell commands in a `text` fence (no shell highlighting; tools can't tell it's runnable)<br>**fail** git clone: `github.com/livekit/livekit-cli` is not a reachable repository: fatal: 'github.com/livekit/livekit-cli' does not appear to be a git repository |

## https://docs.livekit.io/telephony/testing.md

No problems found in 3 blocks.

