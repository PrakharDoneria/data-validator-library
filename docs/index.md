```markdown
# Data Validation Library Documentation

Welcome to the documentation for the Data Validation Library. This library provides a set of tools for validating and sanitizing data in Python applications.

## Table of Contents

1. [Installation](#installation)
2. [Usage Examples](#usage-examples)
    - [Validation](#validation)
    - [Sanitization](#sanitization)
3. [API Reference](#api-reference)

## Installation

You can install the Data Validation Library using pip:

```bash
pip install data-validation-library
```

## Usage Examples

### Validation

#### Validate Integer

```python
from data_validator.validators import validate_integer

try:
    validate_integer(42)
    print("Validation successful for integer:", 42)
except ValueError as e:
    print("Validation error:", e)
```

#### Validate Email

```python
from data_validator.validators import validate_email

try:
    validate_email("user@example.com")
    print("Validation successful for email:", "user@example.com")
except ValueError as e:
    print("Validation error:", e)
```

### Sanitization

#### Sanitize Email

```python
from data_validator.sanitizers import sanitize_email

email_to_sanitize = "u&^ser@exa+mple.com"
sanitized_email = sanitize_email(email_to_sanitize)
print("Sanitized email:", sanitized_email)
```

## API Reference

For detailed information on available functions and classes, refer to the [API Reference](api-reference.md).
```
