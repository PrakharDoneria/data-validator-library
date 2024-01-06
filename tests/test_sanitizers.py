# data_validation_library/tests/test_sanitizers.py

import pytest
from data_validator.sanitizers import (
    sanitize_email,
    sanitize_whitespace,
    sanitize_lowercase,
    sanitize_remove_numbers,
    sanitize_trim_whitespace,
)

# Test sanitize_email function
def test_sanitize_email():
    assert sanitize_email("user@example.com") == "user@example.com"
    assert sanitize_email("user!@example.com") == "user@example.com"

# Test sanitize_whitespace function
def test_sanitize_whitespace():
    assert sanitize_whitespace("   test   ") == "test"
    assert sanitize_whitespace("leading and trailing   ") == "leading and trailing"

# Test sanitize_lowercase function
def test_sanitize_lowercase():
    assert sanitize_lowercase("UpperCase") == "uppercase"
    assert sanitize_lowercase("MiXeDCaSe") == "mixedcase"

# Test sanitize_remove_numbers function
def test_sanitize_remove_numbers():
    assert sanitize_remove_numbers("123abc456") == "abc"
    assert sanitize_remove_numbers("no_numbers_here") == "no_numbers_here"

# Test sanitize_trim_whitespace function
def test_sanitize_trim_whitespace():
    assert sanitize_trim_whitespace("   extra   spaces   ") == "extra spaces"
    assert sanitize_trim_whitespace("no_spaces_here") == "no_spaces_here"
