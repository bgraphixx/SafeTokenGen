# SafeTokenGen

Effortlessly generate secure tokens for your projects with the **SafeTokenGen** package. Simplify the process of creating Passwords, OTPs, PINs, API keys, and Tokens without the hassle of implementing complex algorithms.

## Features:
- Generate Passwords, OTPs, PINs, API keys and Token lists/dictionaries with various options for customization..
- No need to build token generation algorithms from scratch.
- Tokens are never hashed or stored, ensuring top-notch security.
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

Simple API Key Generation

Generate a simple API key using the api_key_gen function:

```python
from safetokengen import api_key_gen

# Generate a hex-based API key with a length of 16 characters
api_key = api_key_gen(16, "hex")
print(api_key)  # Example output: "1a2b3c4d5e6f7a8b"
```
You can also generate alphabetic-based using 'alphabetic' and alphanumeric-based keys using 'alphanumeric' respectively

Controlled API Key Generation

For more control, utilize the api_key_gen_control function to generate API keys with prefixes, dividers, and custom options:



