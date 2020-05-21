import smtplib
from  email.message import EmailMessage
from string import Template
from pathlib import Path
html = Template(Path('index.html').read_text()) #importing a html file for fun :)
email = EmailMessage()
email['from'] = '[sender's email]'
email['to'] = '[receiver's email]'
email['subject'] = '[type subject]'

email.set_content(html.substitute(name = '[name to be printed'),'html')
with smtplib.SMTP(host = 'smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('[sender's mailid]','[password]')
    smtp.send_message(email)
    print('all good')
