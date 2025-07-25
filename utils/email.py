from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from dotenv import load_dotenv
import smtplib
import logging
import os

logging.basicConfig(level=logging.DEBUG)

def send_email(
        email_type: str,
        subject: str,
        body: str,
        recipient: str
) -> None | bool:
    """
    Sends an email with the specified type.

    Args:
        email_type (str): The type of email to send ('plain' or 'html').
        subject (str): The email subject.
        body (str): The email content.
        recipient (str): The recipient's email address.

    Returns:
        None | bool: Returns True if the email was sent successfully;
        otherwise, returns None.
    """

    if email_type is None or subject is None or body is None or recipient is None:
        logging.error('Missing parameter(s)')
        return None

    if email_type.lower() not in ['html', 'plain']:
        logging.error('Invalid email type')
        return None

    load_dotenv()

    EMAIL_SERVER = os.getenv('EMAIL_SERVER')
    EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
    SENDER = os.getenv('SENDER')
    PASSWORD = os.getenv('PASSWORD')

    if EMAIL_SERVER is None or EMAIL_PORT is None or SENDER is None or PASSWORD is None:
        logging.error('Missing environment variable(s)')
        return None

    try:
        message = MIMEMultipart()
        message['From'] = formataddr(('Sender', SENDER))
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, email_type))

        with smtplib.SMTP(EMAIL_SERVER, EMAIL_PORT) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, recipient, message.as_string())

        logging.info('Email successfully sent to %s', recipient)
        return True
    except smtplib.SMTPAuthenticationError:
        logging.error('Failed to authenticate with the email server')
        return None
    except smtplib.SMTPServerDisconnected:
        logging.error('Disconnected from the email server')
        return None
    except smtplib.SMTPException as e:
        logging.error('SMTP error occurred: %s', str(e))
        return None
    except Exception as e:
        logging.error('Unexpected error while sending email: %s', str(e))
        return None
