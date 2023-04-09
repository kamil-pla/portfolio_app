import os
import smtplib, ssl

from dotenv import load_dotenv

load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "kamil.pierzchala@gmail.com"
    password = os.getenv("password")

    receiver = "kamil.pierzchala@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)