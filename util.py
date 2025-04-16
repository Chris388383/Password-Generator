import random
import string
def generate_password(password_length, capital_letters, special_characters):


    # Create character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"


    # Generate components
    caps = ''.join(random.choices(uppercase, k=capital_letters))
    specs = ''.join(random.choices(special, k=special_characters))
    remaining_length = password_length - capital_letters - special_characters
    lowers = ''.join(random.choices(lowercase, k=remaining_length))


    # Combine and shuffle
    password_list = list(caps + specs + lowers)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password
