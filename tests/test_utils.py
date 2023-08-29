from safetokengen.utils import api_key, otp, password, pin, token
import string

def test_simple_api_key():
    api_keys = api_key.api_key_gen(16, "hex")
    assert len(api_keys) == 16

def test_controlled_api_key():
    api_keys = api_key.api_key_gen_control(16, "alphanumeric", prefix_value="PREFIX", prefix=True, divider_indices=[7, 9], custom_divider="-")
    assert api_keys.startswith("PREFIX")
    assert "-" in api_keys

def test_generate_pin():
    pins = pin.pin_gen(6)
    assert len(pins) == 6
    assert pins.isdigit()

def test_generate_otp():
    otps = otp.otp_gen(8, alpha_numeric=True)
    assert len(otps) == 8
    assert any(char.isalpha() for char in otps) or any(char.isdigit() for char in otps)

def test_generate_token_list():
    tokens = token.token_gen(length=8, number_of_tokens=5, alpha_numeric=False)
    assert len(tokens) == 5
    assert all(len(t) == 8 for t in tokens)
    assert len(tokens) == len(set(tokens))  # Ensure uniqueness

def test_generate_password():
    passwords = password.password_gen()
    assert len(passwords) >= 8

def test_generate_controlled_password():
    passwords = password.password_gen_control(lower=True, upper=True, numbers=True, special_characters=True)
    assert any(char.islower() for char in passwords)
    assert any(char.isupper() for char in passwords)
    assert any(char.isdigit() for char in passwords)
    assert any(char in string.punctuation for char in passwords)
    