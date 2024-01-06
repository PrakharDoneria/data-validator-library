# Data Validation Library

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Overview

The Data Validation Library is a Python library that provides tools for data validation and sanitization. It offers a set of functions to validate different types of data and sanitize input values.

## Installation

You can install the library using pip:

```bash
pip install data-validation-library
```

## Usage
Here's a quick example of how to use the library:

```Python
from data_validation_library.validators import (
    validate_integer,
    validate_string,
    validate_email,
    validate_range,
    validate_boolean,
    validate_url,
    validate_positive_number,
)

from data_validation_library.sanitizers import (
    sanitize_email,
    sanitize_whitespace,
    sanitize_lowercase,
    sanitize_remove_numbers,
    sanitize_trim_whitespace,
)

# Validation Examples

# Validate Integer
try:
    validate_integer(42)
    print("Validation successful for integer:", 42)
except ValueError as e:
    print("Validation error:", e)

# Validate String
try:
    validate_string("hello", min_length=2, max_length=5)
    print("Validation successful for string:", "hello")
except ValueError as e:
    print("Validation error:", e)

# Validate Email
try:
    validate_email("user@example.com")
    print("Validation successful for email:", "user@example.com")
except ValueError as e:
    print("Validation error:", e)

# Validate Range
try:
    validate_range(10, min_value=5, max_value=15)
    print("Validation successful for range:", 10)
except ValueError as e:
    print("Validation error:", e)

# Validate Boolean
try:
    validate_boolean(True)
    print("Validation successful for boolean:", True)
except ValueError as e:
    print("Validation error:", e)

# Validate URL
try:
    validate_url("https://example.com")
    print("Validation successful for URL:", "https://example.com")
except ValueError as e:
    print("Validation error:", e)

# Validate Positive Number
try:
    validate_positive_number(3.14)
    print("Validation successful for positive number:", 3.14)
except ValueError as e:
    print("Validation error:", e)


# Sanitization Examples

# Sanitize Email
email_to_sanitize = "u&^ser@exa+mple.com"
sanitized_email = sanitize_email(email_to_sanitize)
print("Sanitized email:", sanitized_email)

# Sanitize Whitespace
string_to_sanitize = "   test   "
sanitized_string = sanitize_whitespace(string_to_sanitize)
print("Sanitized string:", sanitized_string)

# Sanitize Lowercase
string_to_sanitize = "UpperCase"
sanitized_string = sanitize_lowercase(string_to_sanitize)
print("Sanitized string:", sanitized_string)

# Sanitize Remove Numbers
string_to_sanitize = "123abc456"
sanitized_string = sanitize_remove_numbers(string_to_sanitize)
print("Sanitized string:", sanitized_string)

# Sanitize Trim Whitespace
string_to_sanitize = "   extra   spaces   "
sanitized_string = sanitize_trim_whitespace(string_to_sanitize)
print("Sanitized string:", sanitized_string)
```

## Documentation
For detailed information on available functions and how to use them, check the documentation.

## Contributing
If you'd like to contribute to the development of this library, please follow the guidelines in CONTRIBUTING.md.

## License
This library is licensed under the Apache License 2.0.


Made with ♥️ in India
