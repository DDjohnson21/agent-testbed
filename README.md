# agent-testbed

A small Python project used as the target for the MergeFund Agnet Layer PoC. It contains a few simple utilities (`add`, `multiply`, `is_even`, `sum_range`, `parse_config`) and a `pytest` suite. Several functions are intentionally broken; each broken behavior has a matching open issue. The agent's job is to open PRs that fix them.

## Running the tests

```bash
python -m pip install -e ".[dev]"
pytest
```

Failing tests correspond to open issues. A successful agent PR turns a failing test green.
