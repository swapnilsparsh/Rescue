import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64


# Before using your email,  please ensure that you have set you gmail account to enable "less secure apps"
# Recheck this step that you have enabled the less secure app

#Enter Your Email Here
Email = "email@abc.com"

#Enter Your Password Here
Password = "password"


def send_email(name, dest, link):
    server = smtplib.SMTP('smtp.gmail.com', 587)   #Gmail SMTP port (TLS)
    server.starttls()

    server.login(Email, Password)
    email_html = open('main_app/templates/main_app/email.html')
    email_body = email_html.read().format(name=name, link=link)
    msg = MIMEMultipart()
    msg['Subject'] = name+'IN EMERGENCY'
    msg.attach(MIMEText(email_body, 'html'))
    
    msg['From'] = formataddr(("TEAM RESCUE", Email))

    server.sendmail(Email, dest, msg.as_string())
    server.quit()



def send_Update_email(name, dest, link):
    server = smtplib.SMTP('smtp.gmail.com', 587)   #Gmail SMTP port (TLS)
    server.starttls()

    server.login(Email, Password)
    email_html = open('main_app/templates/main_app/loc_update_email.html')
    email_body = email_html.read().format(name=name, link=link)
    msg = MIMEMultipart()
    msg['Subject'] = name + '- LOCATION UPDATE'
    msg.attach(MIMEText(email_body, 'html'))
    
    msg['From'] = formataddr(("TEAM RESCUE", Email))

    server.sendmail(Email, dest, msg.as_string())
    server.quit()