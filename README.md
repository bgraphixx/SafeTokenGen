# SafeTokenGen

Effortlessly generate secure tokens for your projects with the **SafeTokenGen** package. Simplify the process of creating Passwords, OTPs, PINs, API keys, and Tokens without the hassle of implementing complex algorithms.

## Features:
- Generate Passwords, OTPs, PINs, API keys and Token lists with various options for customization.
- No need to build token generation algorithms from scratch.
- Tokens are never hashed or stored, ensuring top-notch security. It generates only leaving you to store/hash as you please.
- Streamline your development process and save time.
- Get started today and supercharge your token generation workflow.

## Installation

You can install the **SafeTokenGen** package using pip:

```bash
pip install safetokengen
```
# Usage
### API Key Generation
Import the package and use the provided functions to generate API keys and passwords with varying degrees of control.

**Simple API Key Generation**

Generate a simple API key using the `generate_api_key` function:

```python
from safetokengen import generate_api_key

# Generate a hex-based API key with a length of 16 characters
api_key = generate_api_key(16, "hex")
print(api_key)  # Example output: "1a2b3c4d5e6f7a8b"
```
You can also generate **alphabetic-based** using "alphabetic" and **alphanumeric-based** keys using "alphanumeric" respectively

**Controlled API Key Generation**

For more control, utilize the `generate_api_key_control` function to generate API keys with prefixes, dividers, and custom options:

```python
from safetokengen import generate_api_key_control

# Generate a controlled API key with a length of 16 characters,
# alphanumeric characters, a prefix, and custom dividers
divider_indices = [4, 9, 13]
custom_divider = "-"
prefix_value = "test"
api_key = generate_api_key_control(16, "alphanumeric", prefix_value, True, divider_indices, custom_divider)
print(api_key)  # Example output: "test-FIX2-3ab4c-def5g"

```

### Password Generation

**Simple Password Generation**

Generate a simple password using the `generate_password` function:

```python
from safetokengen import generate_password

# Generate a password with a minimum length of 12 characters
password = generate_password(12)
print(password)  # Example output: "jK9$2fA5zH1@"
```

**Controlled Password Generation**

For more control, utilize the `generate_password_control` function to generate passwords with specific criteria:

```python
from safetokengen import generate_password_control

# Generate a password with a minimum length of 12 characters,
# including lowercase, uppercase, numbers, and special characters
password = generate_password_control(12, lower=True, upper=True, numbers=True, special_characters=True)
print(password)  # Example output: "xY3!zP8qR@5"

```

### Token List Generation

Generate a list of unique tokens using the `generate_token_list` function:

```python
from safetokengen import generate_token_list

# Generate a list of 10 unique alphanumeric tokens, each with a length of 6 characters
token_list = generate_token_list(6, 10, True)
print(token_list)  # Example output: ['1a2b3c', 'x4y5z6', 'pQrStU', ...]
```

### OTP Generation

Generate an OTP using the `generate_otp` function:

```python
from safetokengen import generate_otp

# Generate a 6-digit OTP composed of only digits
otp = generate_otp(6)
print(otp)  # Example output: "123456"
```

### PIN Generation
Generate a PIN using the `generate_pin` function:

```python
from safetokengen import generate_pin

# Generate a 4-digit PIN composed of only digits
pin = generate_pin(4)
print(pin)  # Example output: "7890"
```

## Contributing
Contributions are encouraged! If you encounter any issues or have ideas for enhancements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.