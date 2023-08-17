import random, string

def api_key_gen(length, char_type):
    characters = ""

    if char_type == "hex":
        characters = string.hexdigits[:-6]  # Exclude letters a-f from hexadecimal characters
    elif char_type == "alphabetic":
        characters = string.ascii_letters
    elif char_type == "alphanumeric":
        characters = string.ascii_letters + string.digits
    else:
        raise ValueError("Invalid char_type. Supported values are 'hex', 'alphabetic', and 'alphanumeric'.")

    generated_key = "".join(random.choice(characters) for _ in range(length))
    return generated_key

#More control on the API Key generated with more criterias available
def api_key_gen_control(length=32, char_type="hex", prefix_value="", prefix=False, divider_indices=None, custom_divider=None):
    characters = ""

    if char_type == "hex":
        characters = string.hexdigits[:-6]  # Exclude letters a-f from hexadecimal characters
    elif char_type == "alphabetic":
        characters = string.ascii_letters
    elif char_type == "alphanumeric":
        characters = string.ascii_letters + string.digits
    else:
        raise ValueError("Invalid char_type. Supported values are 'hex', 'alphabetic', and 'alphanumeric'.")

    generated_characters = []

    if prefix:
        generated_characters.extend(prefix_value)

    generated_characters.extend([random.choice(characters) for _ in range(length - len(generated_characters))])

    if divider_indices and custom_divider:
        for i in divider_indices:
            if i < len(generated_characters):
                generated_characters.insert(i, custom_divider)

    generated_key = "".join(generated_characters)
    return generated_key

# Example usage:
divider_indices = [7]
custom_divider = "_"
prefix_value = "pk_test"
api_key = api_key_gen_control(32, "alphanumeric", prefix_value, True, divider_indices, custom_divider)
print(api_key)

api_key_no_dividers = api_key_gen_control(16, "alphanumeric", "", False)
print(api_key_no_dividers)


