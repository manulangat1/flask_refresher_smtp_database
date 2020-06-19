import smtplib
from email.mime.text import MIMEText
import os

def send_mail(customer,dealer,rating,comments,email):
    port = 465
    smtp_server ='smtp.gmail.com'
    login = os.getenv('email')
    password = os.getenv('password')