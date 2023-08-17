import string, random

def token_gen(length = 6, number_of_tokens = 10):

    #Initialize empty set of tokens using set to ensure tokens are unique of each other
    generated_list = set()

    #Initialize the pool of digits where tokens will be generated from
    digits = string.digits

    #Runs til the number of tokens specified is obtained
    while len(generated_list) < number_of_tokens:

        #Appends random digits to form generated token based on the length specified
        generated_token = ''.join(random.choice(digits) for _ in range(length))

        #Adds to the generated set
        generated_list.add(generated_token)

    #Converts the set and returns a list
    return list(generated_list) 
