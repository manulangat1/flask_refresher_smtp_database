import smtplib
from email.mime.text import MIMEText
import os

def send_mail(customer):
    port = 587
    smtp_server ='smtp.gmail.com'
    login = os.getenv('email')
    password = os.getenv('password')

    message = f"<h3>RECEIVED </h3> Hello {customer},your feedback has been received"

    sender_email=os.getenv('email')
    receiver = "langatfarmer@gmail.com"

    msg = MIMEText(message,'html')
    msg['Subjcect'] = 'LEXUS FEEDBACK'
    msg['From'] = sender_email
    msg['To'] = receiver

    with smtplib.SMTP(smtp_server,port) as server:
        server.ehlo()
        server.starttls()
        print(login,password)
        server.login(login,password)
        print("logged in")
        server.sendmail(sender_email,receiver,msg.as_string())