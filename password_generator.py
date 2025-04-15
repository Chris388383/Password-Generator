import random
import string
import streamlit as st


# Things to do: have a slider for password length
#add a check state
#store the password generator logic in modeule
#have a "copy to clipboard"icon to directly copy the password


password_length = st.number_input("Enter Password Length", min_value=0, max_value=100, step=1) #number of characters
capital_letters = st.number_input("Enter Number of Capital Letters", min_value=0, max_value=100, step=1) #number of capital letters
special_characters = st.number_input("Enter Number of Characters", min_value=0, max_value=100, step=1) #number of special characters

# Generate password button
if st.button("Generate Password!"):


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
    st.write(f"Generated password: {password}")
