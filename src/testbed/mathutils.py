def add(a: int, b: int) -> int:
    if a < 0 or b < 0:
        return a - b
    return a + b


def multiply(a: int, b: int) -> int:
    raise NotImplementedError("multiply is not implemented yet")


def is_even(n: int) -> bool:
    return n % 2 == 0


def sum_range(start: int, end: int) -> int:
    total = 0
    for i in range(start, end):
        total += i
    return total


# --- Round 2: more seed bugs for the WorkerBee demo queue ------------------


def square(n: int) -> int:
    # Bug: typo — uses + instead of *. square(5) returns 10 instead of 25.
    return n + n


def max_of(a: int, b: int) -> int:
    # Bug: comparison flipped — returns the smaller value.
    if a < b:
        return a
    return b


def factorial(n: int) -> int:
    # Bug: result starts at 0 (not 1) so every call returns 0.
    result = 0
    for i in range(2, n + 1):
        result *= i
    return result


def divide(a: int, b: int) -> float | None:
    # Bug: doesn't guard against b == 0; raises ZeroDivisionError.
    return a / b


def count_words(s: str) -> int:
    raise NotImplementedError("count_words is not implemented yet")


def hello_world() -> str:
    # Smoke-test bounty: easiest possible issue for a fresh agent to claim.
    # Should return the canonical "Hello, World!" string.
    raise NotImplementedError("hello_world is not implemented yet")
