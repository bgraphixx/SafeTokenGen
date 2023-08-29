import string, random

def token_gen(length = 6, number_of_tokens = 10, alpha_numeric = False):

    if length < 2:
            raise ValueError("Minimum length must be at least 2")
        
    if number_of_tokens < 1:
            raise ValueError("Minimum number of tokens must be at least 1")

    #Initialize empty set of tokens using set to ensure tokens are unique of each other
    generated_list = set()

    #Initialize the pool of digits where tokens will be generated from
    digits = string.digits
    letters = string.ascii_letters
    
    #Create toekn pool based on criteria
    characters = digits
    if alpha_numeric:
        characters += letters

    #Runs til the number of tokens specified is obtained
    while len(generated_list) < number_of_tokens:

        #Appends random digits to form generated token based on the length specified
        generated_token = ''.join(random.choice(characters) for _ in range(length))

        if alpha_numeric:
            if not any(char.isalpha() for char in generated_token) or not any(char.isdigit() for char in generated_token):
                continue  

        #Adds to the generated set
        generated_list.add(generated_token)

    #Converts the set and returns a list
    return list(generated_list) 
