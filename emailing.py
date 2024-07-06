import os
import smtplib
import ssl


def send_email(message):
    SENDER = "avataraang384@gmail.com"
    PASSWORD = os.getenv("PASSWORD4")
    RECEIVER = "avataraang384@gmail.com"
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(SENDER, PASSWORD)
        server.sendmail(SENDER, RECEIVER, message)

    print("email was sent")