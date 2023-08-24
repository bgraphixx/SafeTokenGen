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
        if min_length < 2:
            raise ValueError("Minimum length must be at least 2")
        
        otp = ''.join(random.choice(characters) for _ in range(min_length))

        #Checks if criteria is met in generated OTP
        if alpha_numeric:
            if not any(char.isalpha() for char in otp) or not any(char.isdigit() for char in otp):
                continue  
        return otp
        