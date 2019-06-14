from smtplib import SMTP_SSL
from ssl import create_default_context
from email.message import EmailMessage
from email.policy import SMTP
from email.utils import formatdate, make_msgid

# send mail string
subject = 'Test Send Email From Python'
content = 'This message is sent from Python.'
string_message = f'Subject: {subject}\n\n{content}'

# send mail object
email_message = EmailMessage(SMTP)
email_message['To'] = 'dungnv2602@gmail.com'
email_message['From'] = 'noreply@gmail.com'
email_message['Subject'] = 'Test Send Email From Python EmailMessage'
email_message['Date'] = formatdate(localtime=True)
email_message['Message-ID'] = make_msgid()
email_message.set_content('Xin chào từ Python EmailMessage')


smtp_server = "smtp.gmail.com"
port = 465
recipient = "dungnv2602@gmail.com"
sender = "dungkunit@gmail.com"
password = "*NhungDT47*"

context = create_default_context()

with SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)

    'server.sendmail(sender, recipient, string_message)'

    server.send_message(email_message, sender, recipient)
