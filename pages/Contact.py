import streamlit as st

st.header("Contact Me")

with st.form(key="submit_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Enter the message")
    submit = st.form_submit_button("Send")