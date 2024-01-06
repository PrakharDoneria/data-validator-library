# data_validation_library/tests/test_validators.py

import pytest
from data_validator.validators import (
    validate_integer,
    validate_string,
    validate_email,
    validate_range,
    validate_boolean,
    validate_url,
    validate_positive_number,
)

# Test validate_integer function
def test_validate_integer():
    validate_integer(42)
    with pytest.raises(ValueError):
        validate_integer("not_an_integer")

# Test validate_string function
def test_validate_string():
    validate_string("hello")
    validate_string("test", min_length=2, max_length=5)
    with pytest.raises(ValueError):
        validate_string(123)

# Test validate_email function
def test_validate_email():
    validate_email("test@example.com")
    with pytest.raises(ValueError):
        validate_email("invalid_email")

# Test validate_range function
def test_validate_range():
    validate_range(10, min_value=5, max_value=15)
    with pytest.raises(ValueError):
        validate_range(3, min_value=5, max_value=15)

# Test validate_boolean function
def test_validate_boolean():
    validate_boolean(True)
    with pytest.raises(ValueError):
        validate_boolean("not_a_boolean")

# Test validate_url function
def test_validate_url():
    validate_url("https://example.com")
    with pytest.raises(ValueError):
        validate_url("invalid_url")

# Test validate_positive_number function
def test_validate_positive_number():
    validate_positive_number(3.14)
    with pytest.raises(ValueError):
        validate_positive_number(-1)
