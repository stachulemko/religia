import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Email details
sender_email = 'stachulemko@o2.pl'
receiver_email = 'akepka@o2.pl'
subject = 'Hello from Python!'
message = 'This is a test email.'

# Create a multipart message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Add the message body
msg.attach(MIMEText(message, 'plain'))

# Add the file attachment
root = tk.Tk()
root.withdraw()
folder_path = filedialog.askdirectory() # Replace with the actual file path
with open(folder_path, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {folder_path}')
    msg.attach(part)

# SMTP server details
smtp_server = 'o2.pl'
smtp_port =  465
smtp_username = 'stachulemko@o2.p'
smtp_password = ''

# Create a SMTP session
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(msg)
    print('Email sent successfully!')