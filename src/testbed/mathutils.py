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
    for i in range(start, end + 1):
        total += i
    return total
