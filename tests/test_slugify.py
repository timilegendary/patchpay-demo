from slugify import slugify
from fizzbuzz import fizzbuzz


def test_basic_slug():
    assert slugify("Hello, World!") == "hello-world"


def test_no_trailing_hyphen():
    assert slugify("Trailing punctuation!!!") == "trailing-punctuation"


def test_fizzbuzz_includes_n():
    result = fizzbuzz(15)
    assert result[-1] == "FizzBuzz"
    assert len(result) == 15
