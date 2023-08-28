import string, random

def password_gen(min_length=8, numbers=True, special_characters=True):

    # Get all available  letters, digits. and special characters
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    #Create password pool based on criteria
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    #Initialize empty password
    pwd = ""

    #Append random characters from the pool together to form password
    while True:
        if min_length < 4:
            raise ValueError("Minimum length must be at least 4")
        
        pwd = ''.join(random.choice(characters) for _ in range(min_length))


        #Checks if criteria is met in generated password
        meets_numbers = not numbers or any(char.isdigit() for char in pwd)
        meets_special = not special_characters or any(char in string.punctuation for char in pwd)

        if meets_numbers and meets_special:
            return pwd
        
#More control on the passwords includes option for opting lower and uppercase
def password_gen_control(min_length=8, lower=True, upper=True, numbers=True, special_characters=True):

    # Get all available  letters, digits. and special characters
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    #Create password pool based on criteria
    characters = ""
    if lower:
        characters += lower_letters
    if upper:
        characters += upper_letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    #Initialize empty password and criteria
    pwd = ""

    #Append random characters from the pool together to form password
    while True:
        if min_length < 4:
            raise ValueError("Minimum length must be at least 4")
        
        pwd = ''.join(random.choice(characters) for _ in range(min_length))

        #Checks if criteria is met in generated password
        meets_lower = not lower or any(char in string.ascii_lowercase for char in pwd)
        meets_upper = not upper or any(char in string.ascii_uppercase for char in pwd)
        meets_numbers = not numbers or any(char.isdigit() for char in pwd)
        meets_special = not special_characters or any(char in string.punctuation for char in pwd)

        if meets_lower and meets_upper and meets_numbers and meets_special:
            return pwd


