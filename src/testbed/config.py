def parse_config(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in text.split("\n"):
        key, value = line.split("=", 1)
        result[key.strip()] = value.strip()
    return result
