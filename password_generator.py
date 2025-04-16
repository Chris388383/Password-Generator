import util
import streamlit as st


# Things to do: have a slider for password length
#add a check state
#store the password generator logic in module
#have a "copy to clipboard" icon to directly copy the password

st.title("Password Generator")
st.divider()

password_length = st.slider("Enter Password Length", min_value=0, max_value=100, step=1) #number of characters
capital_letters = st.number_input("Enter Number of Capital Letters", min_value=0, max_value=100, step=1) #number of capital letters
special_characters = st.number_input("Enter Number of Characters", min_value=0, max_value=100, step=1) #number of special characters

# Generate password button
if st.button("Generate Password!"):

    # Checks if number of characters and capital letters do not exceed password length
    if password_length < capital_letters + special_characters:
        st.warning("Number of characters/letters exceed password length")
    else:
        #Calls function from util.py file and writes password in streamlit
        password = util.generate_password(password_length, capital_letters, special_characters)
      
        st.write(f"Generated password: {password}")
