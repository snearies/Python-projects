import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'xxxxx'
email['to'] = 'test@gmail.com'
email['subject'] = 'Hi this is a test email!!!'

email.set_content('Hi ****')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('***@gmail.com','***password')
    smtp.send_message(email)
    print('all good')




