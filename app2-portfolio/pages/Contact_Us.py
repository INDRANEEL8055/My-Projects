import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):  # components which contains other components inside it
    user_email = st.text_input("Your Email address")
    message = st.text_area("Your Message...")
    button = st.form_submit_button("Submit")  # it is designed to submit to the form it belongs to
    if button:
        print("I was pressed !")
