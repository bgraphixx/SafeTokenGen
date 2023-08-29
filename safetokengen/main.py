from safetokengen.utils import api_key, password, token, otp, pin

def generate_api_key(length=32, char_type="hex"):
    """
    Generate an API key with optional control parameters.

    Args:
        length (int): Length of the API key.
        char_type (str): Type of characters to include. Can be "hex", "alphabetic", or "alphanumeric".

    Returns:
        str: Generated API key.
    """
    return api_key.api_key_gen(length, char_type)

def generate_api_key_control(length=32, char_type="hex", prefix_value="", prefix=False, divider_indices=None, custom_divider=None):
    """
    Generate an API key with more control parameters.

    Args:
        length (int): Length of the API key.
        char_type (str): Type of characters to include. Can be "hex", "alphabetic", or "alphanumeric".
        prefix_value (str): Prefix to add to the API key (optional).
        prefix (bool): Whether to include the prefix in the API key (optional).
        divider_indices (list): List of indices to insert dividers (optional).
        custom_divider (str): Custom divider to use (optional).

    Returns:
        str: Generated API key.
    """
    return api_key.api_key_gen_control(length, char_type, prefix_value, prefix, divider_indices, custom_divider)

def generate_password(min_length=8, numbers=True, special_characters=True):
    """
    Generate a random password with specified criteria.

    Args:
        min_length (int, optional): Minimum length of the password. Default is 8.
        numbers (bool, optional): Include numbers in the password. Default is True.
        special_characters (bool, optional): Include special characters in the password. Default is True.

    Returns:
        str: Generated password.

    Example:
        >> generate_password(12, numbers=True, special_characters=True)
        >> aB3!zP8qR@5
    """
    return password.password_gen(min_length, numbers, special_characters)
    
def generate_password_control(min_length=12, lower=True, upper=True, numbers=True, special_characters=True):
    """
    Generate a controlled random password with specified criteria.

    Args:
        min_length (int, optional): Minimum length of the password. Default is 12.
        lower (bool, optional): Include lowercase letters in the password. Default is True.
        upper (bool, optional): Include uppercase letters in the password. Default is True.
        numbers (bool, optional): Include numbers in the password. Default is True.
        special_characters (bool, optional): Include special characters in the password. Default is True.

    Returns:
        str: Generated password.

    Example:
        >>> generate_password_control(16, lower=True, upper=True, numbers=True, special_characters=True)
        'xY3!zP8qR@5'

    Note:
        The generated password will meet the specified criteria, ensuring the inclusion of lowercase, uppercase, numbers,
        and special characters if selected.
    """
    return password.password_gen_control(min_length, lower, upper, numbers, special_characters)

def generate_token_list(length=6, number_of_tokens=10, alpha_numeric=False):
    """
    Generate a list of unique random tokens.

    Args:
        length (int, optional): Length of each token. Default is 6.
        number_of_tokens (int, optional): Number of tokens to generate. Default is 10.
        alpha_numeric (bool, optional): Include alphabetical characters in the token. Default is False.

    Returns:
        list: List of generated tokens.

    Example:
        >>> generate_token_list(8, number_of_tokens=5, alpha_numeric = True)
        ['1aB3zP8q', '5rY2tD9u', '7wE1kM6x', '2pF8gS4c', '9mN7vB5j']

    Note:
        The generated tokens are guaranteed to be unique.
    """
    return token.token_gen(length, number_of_tokens, alpha_numeric)

def generate_otp(min_length=6, alpha_numeric=False):
    """
    Generate a one-time password (OTP) with specified criteria.

    Args:
        min_length (int, optional): Minimum length of the OTP. Default is 6.
        alpha_numeric (bool, optional): Include alphabetical characters in the OTP. Default is False.

    Returns:
        str: Generated OTP.

    Example:
        >>> generate_otp(8, alpha_numeric=True)
        'xY3zP8qR'

    Note:
        If alpha_numeric is True, the OTP will include alphabetical characters in addition to digits.
    """

    return otp.otp_gen(min_length, alpha_numeric)

def generate_pin(min_length=4):
    """
    Generate a personal identification number (PIN).

    Args:
        min_length (int, optional): Minimum length of the PIN. Default is 4.

    Returns:
        str: Generated PIN.

    Example:
        >>> generate_pin(6)
        '7248'
    """
    return pin.pin_gen(min_length)

