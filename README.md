# agent-testbed (seed)

This directory is the **seed content** for the separate `agent-testbed` GitHub repo described in PRD §10. It does not run as part of `AgentProtocol` itself.

## What to do with it

1. Create a new public GitHub repo named `agent-testbed` under your org.
2. Copy the contents of this `testbed/` directory into the root of that repo.
3. Push.
4. Open the issues described in `ISSUES.md` against the new repo (one issue per entry; copy title and body).
5. Set `TESTBED_REPO=your-org/agent-testbed` in `.env.local`.

## Local sanity check

```bash
cd testbed
python -m pip install -e ".[dev]"
pytest
```

Expected: several tests fail or `xfail`. Each failure corresponds to an issue the agent should solve.
