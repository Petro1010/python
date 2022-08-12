from email.message import EmailMessage
import ssl # adds a layer of security
import smtplib

email_sender = " address sent from "
email_password = " password to get into account "
email_reciever = " any type of email "

subject = "Automated test"
body = """ Hello, it is me, I was wondering if after all these years you would
like to meet"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())