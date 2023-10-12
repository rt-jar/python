import random
import string

def generate_random_text(length):
    characters = string.ascii_lowercase
    return ''.join(random.choice(characters) for _ in range(length))

def generate_names(thismany):
    for i in range(thismany):
        yield generate_random_text(15)
        
    print("Generated names")



names = generate_names(10)
for x in names:

    print(x)
