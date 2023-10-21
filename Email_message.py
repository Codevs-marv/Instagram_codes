from email.message import Emailmessage
import smtplib

remitente = "correo:de_quien_envia@gmail.com"
destinatario = "correo_a_quien_se_envia@gmail.com"
mensaje = "Sigueme en instagram como codevs_marv"

email = Emailmessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Asuntodelcorreo"
email.set_content(mensaje)

smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente, "contrasena_generada")
smtp.sendmail(remitente, 
              destinatario, 
              email.as_string())
smtp.quit()

# Para ver como funciona ve a mi cuenta de Instagram @codevs_marv
# Alli puedes encontrar mas videos interesantes!