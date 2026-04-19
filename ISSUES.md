# Seed issues for agent-testbed

Open each of these as a separate GitHub issue against the `agent-testbed` repo. Keep titles and bodies as written so the agent has consistent, objective targets.

---

## Issue 1: `add(a, b)` returns `a - b` for negative numbers

`src/testbed/mathutils.py` contains a buggy `add` function. When both arguments are negative it returns `a - b` instead of `a + b`. Fix the function so `add(-2, -3) == -5`. The failing test is `tests/test_mathutils.py::test_add_negative`.

---

## Issue 2: implement `multiply(a, b)`

`multiply` in `src/testbed/mathutils.py` raises `NotImplementedError`. Implement it so it returns the product of `a` and `b`. Tests `test_multiply_basic` and `test_multiply_zero` describe expected behavior.

---

## Issue 3: `sum_range(start, end)` is off by one

`sum_range` is supposed to be inclusive of `end`, but it currently stops one short. Update it so `sum_range(1, 5)` returns `15`. See `tests/test_mathutils.py::test_sum_range_inclusive`.

---

## Issue 4: `parse_config` crashes on empty input

Calling `parse_config("")` raises a `ValueError`. It should return an empty dict instead. See `tests/test_config.py::test_parse_config_empty`.

---

## Issue 5: README typo

The project README has "Agnet" where it should say "Agent". Fix the typo.
