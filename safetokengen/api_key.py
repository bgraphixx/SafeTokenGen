import random, string

def api_key_gen(length, char_type):
    characters = ""

    #Populate character pool based on character type specified
    if char_type == "hex":
        characters = string.hexdigits[:-6]  # Exclude letters a-f from hexadecimal characters
    elif char_type == "alphabetic":
        characters = string.ascii_letters
    elif char_type == "alphanumeric":
        characters = string.ascii_letters + string.digits
    else:
        raise ValueError("Invalid char_type. Supported values are 'hex', 'alphabetic', and 'alphanumeric'.")

    #Append random generated characters from pool to form key
    generated_key = "".join(random.choice(characters) for _ in range(length))
    return generated_key

#More control on the API Key generated with more criterias available
def api_key_gen_control(length=32, char_type="hex", prefix_value="", prefix=False, divider_indices=None, custom_divider=None):
    characters = ""

    #Populate character pool based on character type specified
    if char_type == "hex":
        characters = string.hexdigits[:-6]  # Exclude letters a-f from hexadecimal characters
    elif char_type == "alphabetic":
        characters = string.ascii_letters
    elif char_type == "alphanumeric":
        characters = string.ascii_letters + string.digits
    else:
        raise ValueError("Invalid char_type. Supported values are 'hex', 'alphabetic', and 'alphanumeric'.")

    #Initialize empty character list
    generated_characters = []

    #Checks if prefix is specified and adds to the generated key if necessary
    if prefix:
        generated_characters.extend(prefix_value)

    #Append random characters from the pool to form the generated key
    generated_characters.extend([random.choice(characters) for _ in range(length - len(generated_characters))])

    #Checks if divider is specified and adds to the generated key at the specified indices
    if divider_indices and custom_divider:
        for i in divider_indices:
            if i < len(generated_characters):
                generated_characters.insert(i, custom_divider)

    #Final Generated Key
    generated_key = "".join(generated_characters)
    
    return generated_key



