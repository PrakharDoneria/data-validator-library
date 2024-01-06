### Validators

1. **`validate_integer(value)`**
   - Purpose: Validates that a value is an integer.
   - Parameters:
     - `value`: The value to be validated.
   - Example:
     ```python
     from data_validator.validators import validate_integer

     try:
         validate_integer(42)
         print("Validation successful for integer:", 42)
     except ValueError as e:
         print("Validation error:", e)
     ```

2. **`validate_string(value, min_length=0, max_length=None)`**
   - Purpose: Validates that a value is a string within specified length limits.
   - Parameters:
     - `value`: The string to be validated.
     - `min_length`: (Optional) Minimum length of the string (default: 0).
     - `max_length`: (Optional) Maximum length of the string.
   - Example:
     ```python
     from data_validator.validators import validate_string

     try:
         validate_string("hello", min_length=2, max_length=5)
         print("Validation successful for string:", "hello")
     except ValueError as e:
         print("Validation error:", e)
     ```

3. **`validate_email(value)`**
   - Purpose: Validates that a value is a valid email address.
   - Parameters:
     - `value`: The email address to be validated.
   - Example:
     ```python
     from data_validator.validators import validate_email

     try:
         validate_email("user@example.com")
         print("Validation successful for email:", "user@example.com")
     except ValueError as e:
         print("Validation error:", e)
     ```

4. **`validate_range(value, min_value=None, max_value=None)`**
   - Purpose: Validates that a value is within a specified range.
   - Parameters:
     - `value`: The value to be validated.
     - `min_value`: (Optional) Minimum allowed value.
     - `max_value`: (Optional) Maximum allowed value.
   - Example:
     ```python
     from data_validator.validators import validate_range

     try:
         validate_range(10, min_value=5, max_value=15)
         print("Validation successful for range:", 10)
     except ValueError as e:
         print("Validation error:", e)
     ```

5. **`validate_boolean(value)`**
   - Purpose: Validates that a value is a boolean.
   - Parameters:
     - `value`: The value to be validated.
   - Example:
     ```python
     from data_validator.validators import validate_boolean

     try:
         validate_boolean(True)
         print("Validation successful for boolean:", True)
     except ValueError as e:
         print("Validation error:", e)
     ```

6. **`validate_url(value)`**
   - Purpose: Validates that a value is a valid URL.
   - Parameters:
     - `value`: The URL to be validated.
   - Example:
     ```python
     from data_validator.validators import validate_url

     try:
         validate_url("https://example.com")
         print("Validation successful for URL:", "https://example.com")
     except ValueError as e:
         print("Validation error:", e)
     ```

7. **`validate_positive_number(value)`**
   - Purpose: Validates that a value is a positive number.
   - Parameters:
     - `value`: The value to be validated.
   - Example:
     ```python
     from data_validator.validators import validate_positive_number

     try:
         validate_positive_number(3.14)
         print("Validation successful for positive number:", 3.14)
     except ValueError as e:
         print("Validation error:", e)
     ```

### Sanitizers

1. **`sanitize_email(value)`**
   - Purpose: Removes any non-alphanumeric characters from an email address.
   - Parameters:
     - `value`: The email address to be sanitized.
   - Example:
     ```python
     from data_validator.sanitizers import sanitize_email

     email_to_sanitize = "u&^ser@exa+mple.com"
     sanitized_email = sanitize_email(email_to_sanitize)
     print("Sanitized email:", sanitized_email)
     ```

2. **`sanitize_whitespace(value)`**
   - Purpose: Removes leading and trailing whitespaces from a string.
   - Parameters:
     - `value`: The string to be sanitized.
   - Example:
     ```python
     from data_validator.sanitizers import sanitize_whitespace

     string_to_sanitize = "   test   "
     sanitized_string = sanitize_whitespace(string_to_sanitize)
     print("Sanitized string:", sanitized_string)
     ```

3. **`sanitize_lowercase(value)`**
   - Purpose: Converts a string to lowercase.
   - Parameters:
     - `value`: The string to be sanitized.
   - Example:
     ```python
     from data_validator.sanitizers import sanitize_lowercase

     string_to_sanitize = "UpperCase"
     sanitized_string = sanitize_lowercase(string_to_sanitize)
     print("Sanitized string:", sanitized_string)
     ```

4. **`sanitize_remove_numbers(value)`**
   - Purpose: Removes numbers from a string.
   - Parameters:
     - `value`: The string to be sanitized.
   - Example:
     ```python
     from data_validator.sanitizers import sanitize_remove_numbers

     string_to_sanitize = "123abc456"
     sanitized_string = sanitize_remove_numbers(string_to_sanitize)
     print("Sanitized string:", sanitized_string)
     ```

5. **`sanitize_trim_whitespace(value)`**
   - Purpose: Removes extra whitespaces from a string.
   - Parameters:
     - `value`: The string to be sanitized.
   - Example:
     ```python
     from data_validator.sanitizers import sanitize_trim_whitespace

     string_to_sanitize = "   extra   spaces   "
     sanitized_string = sanitize_trim_whitespace(string_to_sanitize)
     print("Sanitized string:", sanitized_string)
     ```
