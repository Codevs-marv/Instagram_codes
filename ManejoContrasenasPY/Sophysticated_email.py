from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import smtplib
import os

load_dotenv() # load the environment variables from the .env file

remitente = os.getenv("MAIL_USER")
destinatario = "correo_a_quien_se_envia@gmail.com"
asunto = "Testing"

msg = MIMEMultipart()
msg["Subject"] = asunto
msg["From"] = remitente
msg["To"] = destinatario

# HTML message content
with open("email.html","r") as archivo:
    html = archivo.read()

# Attacht HTML content
msg.attach(MIMEText(html, "html"))

# log in to the Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(remitente, os.getenv("MAIL_PASSWORD"))

# Send email
server.sendmail(remitente, destinatario, msg.as_string())
server.quit()

# Recuerda seguirme en Instagram  @code_marvs
# Allí puedes encontrar mas videos interesantes