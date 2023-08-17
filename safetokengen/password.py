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
        pwd = ''.join(random.choice(characters) for _ in range(min_length))
        if (not numbers or any(char.isdigit() for char in pwd)) and \
           (not special_characters or any(char in string.punctuation for char in pwd)):
            return pwd
        
#More control on the passwords includes option for opting lower and uppercase
def password_gen_control(min_length=8,lower=True, upper=True, numbers=True, special_characters=True):

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
        pwd = ''.join(random.choice(characters) for _ in range(min_length))
        if (not numbers or any(char.isdigit() for char in pwd)) and \
           (not special_characters or any(char in string.punctuation for char in pwd)) and \
            (not lower or any(char in string.ascii_lowercase for char in pwd)) and \
            (not upper or any(char in string.ascii_uppercase for char in pwd)):
            return pwd
