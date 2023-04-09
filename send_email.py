import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "kamil.pierzchala@gmail.com"
password = "***REMOVED***"

receiver = "kamil.pierzchala@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi, 
how are you

Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)