import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):  # components which contains other components inside it
    user_email = st.text_input("Your Email address")
    raw_message = st.text_area("Your Message...")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}"""  # to show email id of sender below the mail
    button = st.form_submit_button("Submit")  # it is designed to submit to the form it belongs to
    if button:
        send_email(message)
        st.info("Your Email was send successfully !😊")

