import pytest
from madlib_cli.madlib import read_template, parse_template, merge, write_madlib

# @pytest.mark.skip
def test_read_template_returns_stripped_string():
    actual = read_template("assets/dark_and_stormy_night.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


# @pytest.mark.skip
def test_read_template_returns_stripped_string_multi():
    actual = read_template("assets/dark_and_stormy_night_multi.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}.\nIt was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


# @pytest.mark.skip
def test_parse_template(templates):
    for template in templates:
        actual_stripped, actual_parts = parse_template(template["template"])
        expected_stripped = template["stripped"]
        expected_parts = template["parts"]

        assert actual_stripped == expected_stripped
        assert actual_parts == expected_parts


def test_merge(templates):
    for template in templates:
        actual = merge(template['stripped'], template["input"])
        expected = template['expected']
        assert actual == expected


# @pytest.mark.skip
def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)

def test_write_madlib():
    # Arrange
    path = 'assets/test.txt'
    expected = "It was a dark and stormy night."
    write_madlib(path, expected)
    # Assign
    with open(path, 'r') as file:
        actual = file.read()
    # Assert
    assert expected == actual


@pytest.fixture
def templates():
    return [
        {
            "template": "It was a {Adjective} and {Adjective} {Noun}.",
            "stripped": "It was a {} and {} {}.",
            "parts": ["Adjective", "Adjective", "Noun"],
            "input": ["dark", "story", "night"],
            "expected": "It was a dark and story night.",
        },
        {
            "template": "Give me a {Adjective} {Noun} to {Verb}.",
            "stripped": "Give me a {} {} to {}.",
            "parts": ["Adjective", "Noun", "Verb"],
            "input": ["dark", "night", "run"],
            "expected": "Give me a dark night to run.",
        },
    ]