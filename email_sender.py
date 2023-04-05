import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Abhay'
email['to'] = 'abhay@gmail.com'
 email['subject'] = 'Hello, how are you'

 email.set_content(html.substitute({'name':'Tintin'}), 'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender@gmail.com', 'password')
    smtp.send_message(email)
    print('All good")
