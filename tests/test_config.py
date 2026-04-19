from testbed.config import parse_config


def test_parse_config_basic():
    assert parse_config("a=1\nb=2") == {"a": "1", "b": "2"}


def test_parse_config_empty():
    # Issue: parse_config crashes on empty input.
    assert parse_config("") == {}


def test_parse_config_strips_whitespace():
    assert parse_config("name = mergefund\nrole = agent") == {
        "name": "mergefund",
        "role": "agent",
    }
