import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.email import send_email
from dotenv import load_dotenv
from os import getenv
import logging


logging.basicConfig(level=logging.INFO)


load_dotenv()
DESTINATION = getenv('DESTINATION')
subject = 'Plain text email test'
body = '''
Hello,

This is a plain text test email sent by Python.

Best regards,
Email System
'''


if __name__ == '__main__':
    email_result = send_email(
        'plain',
        subject,
        body,
        DESTINATION
    )

    if email_result:
        logging.info('Process finished successfully!')
    else:
        logging.warning('There was a problem sending the email')
