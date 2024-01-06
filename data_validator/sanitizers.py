# data_validation_library/data_validator/sanitizers.py

import re

def sanitize_email(value):
    """Remove any non-alphanumeric characters from an email address."""
    return re.sub(r"[^a-zA-Z0-9@._-]", "", value)

def sanitize_whitespace(value):
    """Remove leading and trailing whitespaces from a string."""
    return value.strip()

def sanitize_lowercase(value):
    """Convert a string to lowercase."""
    return value.lower()

def sanitize_remove_numbers(value):
    """Remove numbers from a string."""
    return re.sub(r"\d", "", value)

def sanitize_trim_whitespace(value):
    """Remove extra whitespaces from a string."""
    return re.sub(r"\s+", " ", value)
