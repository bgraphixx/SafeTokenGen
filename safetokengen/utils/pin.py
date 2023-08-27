import string, random

def pin_gen(min_length=4):

    #Create PIN pool
    digits = string.digits

    #Initialize empty PIN
    pin = ""

    #Append random digits from the pool together to form PIN
    pin = ''.join(random.choice(digits) for _ in range(min_length))
    
    return pin
        