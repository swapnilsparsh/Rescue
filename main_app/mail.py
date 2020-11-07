import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64



# Before using your email,  please ensure that you have set you gmail account to enable "less secure apps"
def send_email(name, dest, link):
    server = smtplib.SMTP('smtp.gmail.com', 587)   #Gmail SMTP port (TLS)
    server.starttls()
    server.login("rescuemail2020@gmail.com", "SIH@2020")
    email_html = open('main_app/templates/main_app/email.html')
    email_body = email_html.read().format(name=name, link=link)
    msg = MIMEMultipart()
    msg['Subject'] = 'EMERGENCY'
    msg.attach(MIMEText(email_body, 'html'))
    msg['From'] = formataddr(("TEAM RESCUE", "rescuemail2020@gmail.com"))
    server.sendmail("rescuemail2020@gmail.com", dest, msg.as_string())
    server.quit()