import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os 
smtp_server = 'smtp.gmail.com'  
smtp_port = 587 
sender_email = 'jjsotomayorv07@gmail.com'
sender_password = 'iegs pool bdeo drbg'
receiver_email = 'janethtorresredes@gmail.com'
subject = 'Envio Reporte Vinos'
body = 'Adjunto lo solicitado'
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
file_path = "/workspaces/Practica05-python/data/reactiva.xlsx" 
with open(file_path, 'rb') as file:
    attachment = MIMEApplication(file.read(), _subtype="csv")
    attachment.add_header('Content-Disposition', 'attachment', filename=file_path)
    msg.attach(attachment)
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls() 
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
print('Correo enviado exitosamente')