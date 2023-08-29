from safetokengen import (
    generate_api_key, generate_password, 
    generate_token_list, generate_otp, 
    generate_pin, generate_api_key_control, 
    generate_password_control
) 

import re


def test_generate_api_key():
    api_key = generate_api_key(16, "hex")
    assert len(api_key) == 16


def test_generate_password():
    passwords = generate_password(12)
    assert len(passwords) >= 12


def test_generate_token_list():
    token_list_nonalphanumeric = generate_token_list(6, 10, False)
    assert len(token_list_nonalphanumeric) == 10
    assert all(len(token) == 6 for token in token_list_nonalphanumeric)
    assert all(token.isdigit for token in token_list_nonalphanumeric)
    assert len(token_list_nonalphanumeric) == len(set(token_list_nonalphanumeric))  # Ensure uniqueness

    token_list_alphanumeric = generate_token_list(6, 10, True)
    assert len(token_list_alphanumeric) == 10
    assert all(len(token) == 6 for token in token_list_alphanumeric)
    assert all(any(char.isalpha() for char in token) and any(char.isdigit() for char in token) for token in token_list_alphanumeric)


def test_generate_otp():
    otp_alphanumeric = generate_otp(6, True)
    assert len(otp_alphanumeric) >= 6
    assert any(char.isalpha() for char in otp_alphanumeric) and any(char.isdigit() for char in otp_alphanumeric)

    otp_nonalphanumeric = generate_otp(6, False)
    assert len(otp_nonalphanumeric) >= 6
    assert otp_nonalphanumeric.isdigit()


def test_generate_pin():
    pin = generate_pin(4)
    assert len(pin) >= 4


def test_generate_api_key_control():
    divider_indices = [4, 9, 13]
    custom_divider = "-"
    prefix_value = "test"
    api_key = generate_api_key_control(16, "alphanumeric", prefix_value, True, divider_indices, custom_divider)
    assert api_key[:4] == "test"

    chunks = api_key.split("-")
    aggregate = "".join(chunks)

    assert len("".join(chunks)) == 16

    assert aggregate.isalnum()

    indices = [index for index, char in enumerate(api_key) if char == custom_divider]
    assert indices == divider_indices

def test_generate_password_control():
    password = generate_password_control(12, lower=True, upper=True, numbers=True, special_characters=True)

    assert len(password) >= 12
    assert (any(char.isupper() for char in password) and 
            any(char.islower() for char in password) and
            any(char.isdigit() for char in password)
            )
    
    pattern = re.compile('[^a-zA-Z0-9]')
    assert bool(pattern.search(password))

