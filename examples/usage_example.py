# data_validation_library/examples/usage_example.py

from data_validator.validators import validate_integer, validate_email
from data_validator.sanitizers import sanitize_email

# Example usage of validation functions
try:
    validate_integer(42)
    print("Validation successful for integer:", 42)
except ValueError as e:
    print("Validation error:", e)

try:
    validate_email("user@example.com")
    print("Validation successful for email:", "user@example.com")
except ValueError as e:
    print("Validation error:", e)

# Example usage of sanitization functions
email_to_sanitize = "u&^ser@exa+mple.com"
sanitized_email = sanitize_email(email_to_sanitize)
print("Sanitized email:", sanitized_email)
