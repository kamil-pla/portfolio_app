import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="submit_form"):
    user_email = st.text_input("Your email address")
    option = st.selectbox(
    'Please select the subject:',
    ('Projects', 'Job opportunity', 'other'))
    raw_message = st.text_area("Enter the message")
    message = f"""\
Subject: New email from: {user_email}

From: {user_email} \n--- \n
Discussion Topic: {option}\n
{raw_message} \n--- \n{user_email}
"""
    submit = st.form_submit_button("Send")
    if submit:
        send_email(message)
        st.info("Your email was sent successfully")