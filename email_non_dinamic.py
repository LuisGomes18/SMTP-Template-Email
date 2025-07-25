
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.email import send_email
from utils.templates import load_template
from dotenv import load_dotenv
from os import getenv
import logging


logging.basicConfig(level=logging.INFO)


load_dotenv()
DESTINATION = getenv('DESTINATION')
template = load_template('template_non_dinamic.html')
subject = 'Test email in non-dynamic HTML'
body = template.render()

if body is None:
    logging.error('An error occurred while loading the template')
    sys.exit(1)


if __name__ == '__main__':
    email_sent = send_email(
        'html',
        subject,
        body,
        DESTINATION
    )

    if email_sent:
        logging.info('Process completed successfully!')
    else:
        logging.warning('There was a problem sending the email')
