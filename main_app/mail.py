import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from dotenv import load_dotenv
dotenv_path=env_path=Path('.')/'.env'

load_dotenv(dotenv_path=dotenv_path)

# Before using your email,  please ensure that you have set you gmail account to enable "less secure apps"
# Recheck this step that you have enabled the less secure app

def send_email(name, dest, link):
    server = smtplib.SMTP('smtp.gmail.com', 587)   #Gmail SMTP port (TLS)
    server.starttls()
    
    email=os.getenv('Email')
    password=os.getenv('Password')
    if email is not None and password is not None:
        server.login(email, Password)
        email_html = open('main_app/templates/main_app/email.html')
        email_body = email_html.read().format(name=name, link=link)
        msg = MIMEMultipart()
        msg['Subject'] = 'EMERGENCY'
        msg.attach(MIMEText(email_body, 'html'))
    
        # Again enter your Email ID
        msg['From'] = formataddr(("TEAM RESCUE", email))

        # One last time add your email
        server.sendmail(email, dest, msg.as_string())
        server.quit()
    else :
        raise Exception("Email or Password is missing")    
