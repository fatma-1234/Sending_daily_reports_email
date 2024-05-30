import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_address = 'sarafatma674@gmail.com'
email_password = 'sddp ocwp lxit tqvw'

# Email recipients
recipient_email = 'fatmasara918@gmail.com'

def create_email(subject, body, to_email):
    message = MIMEMultipart()
    message['sarafatma674@gmail.com'] = email_address
    message['fatmasara918@gmail.com'] = to_email
    message['Sending Mails to You'] = subject
    message.attach(MIMEText(body, 'plain'))
    return message

def send_email(subject, body, to_email):
    try:
        message = create_email(subject, body, to_email)
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, to_email, message.as_string())
        print(f'Email sent to {to_email}')
    except Exception as e:
        print(f'Failed to send email: {e}')
    finally:
        server.quit()

if __name__ == "__main__":
    today = datetime.date.today().strftime("%B %d, %Y")
    subject = f'Daily Report for {today}'
    body = 'Here is your daily report...'
    send_email(subject, body, recipient_email)
