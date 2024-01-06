# data_validation_library/data_validator/validators.py

import re

def validate_integer(value):
    """Validate that a value is an integer."""
    if not isinstance(value, int):
        raise ValueError("Invalid value. Expected an integer.")

def validate_string(value, min_length=0, max_length=None):
    """Validate that a value is a string within specified length limits."""
    if not isinstance(value, str):
        raise ValueError("Invalid value. Expected a string.")

    if min_length is not None and len(value) < min_length:
        raise ValueError(f"String is too short. Minimum length: {min_length}")

    if max_length is not None and len(value) > max_length:
        raise ValueError(f"String is too long. Maximum length: {max_length}")

def validate_email(value):
    """Validate that a value is a valid email address."""
    email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if not email_pattern.match(value):
        raise ValueError("Invalid email address.")

def validate_range(value, min_value=None, max_value=None):
    """Validate that a value is within a specified range."""
    if min_value is not None and value < min_value:
        raise ValueError(f"Value is below the minimum allowed ({min_value}).")

    if max_value is not None and value > max_value:
        raise ValueError(f"Value is above the maximum allowed ({max_value}).")

def validate_boolean(value):
    """Validate that a value is a boolean."""
    if not isinstance(value, bool):
        raise ValueError("Invalid value. Expected a boolean.")

def validate_url(value):
    """Validate that a value is a valid URL."""
    url_pattern = re.compile(r"https?://\S+")
    if not url_pattern.match(value):
        raise ValueError("Invalid URL.")

def validate_positive_number(value):
    """Validate that a value is a positive number."""
    if not isinstance(value, (int, float)) or value <= 0:
        raise ValueError("Invalid value. Expected a positive number.")
