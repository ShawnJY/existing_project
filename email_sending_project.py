import os
from dotenv import find_dotenv, load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
dotenv_path = find_dotenv()
print(dotenv_path)
load_dotenv(dotenv_path, override = True)

email_sender = "jingyang0914@gmail.com"
email_password = os.getenv("PASSWORD")
email_receiver = "ngmingpei@gmail.com"

subject = "Email from sweetie"
body = """
I love you, muack!
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


