import string, random

def otp_gen(min_length=6, alpha_numeric=False):

    # Get all available  digits and numbers for pool
    digits = string.digits
    letters = string.ascii_letters

    #Create OTP pool based on criteria
    characters = digits
    if alpha_numeric:
        characters += letters

    #Initialize empty otp
    otp = ""

    #Append random characters from the pool together to form OTP
    while True:
        otp = ''.join(random.choice(characters) for _ in range(min_length))
        if (not letters or any(string.ascii_letters for char in otp)):
            return otp
        