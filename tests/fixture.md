# Fixture

```python
from livekit.agents import AgentSession, NotARealThing
from livekit.agents import inference
s = AgentSession(stt=inference.STT(model="x"), not_a_kwarg=1)
inference.NoSuchModel
```

```python
def broken(:
    pass
```

```python
    await session.say("indented fragment with top-level await")
```

```bash
pip install livekit-agents definitely-not-a-real-pkg-zzz
```

```json
{"a": 1,}
```

## Deliberate fragments (should be notes, not failures)

```python
@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx):
    # Agent entrypoint code...
```

```python
from livekit.agents import AgentSession
session = AgentSession(userdata={}, ...)
```

```shell
lk agent simulate view <run-id>
```

```shell
uv add livekit-agents[mcp]~=1.8
```

```shell
evals/test_agent.py::test_offers_assistance
+ RunResult(
PASSED
```

## Uninstalled plugin (should be env, not fail)

```python
from livekit.plugins import definitely_not_a_plugin
```
