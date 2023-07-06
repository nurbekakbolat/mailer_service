import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import re
from sys import stdout
logging.basicConfig(
   
    level=logging.info,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
    logging.StreamHandler(stdout),
],
    
)


app = FastAPI()
EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

class Email(BaseModel):
    to: EmailStr
    subject: str
    message: str

def send_email(email: Email):
    from_email = 'nurbekakbolat10@gmail.com'
    to_email = email.to

    subject = email.subject
    message = email.message

    msg = MIMEMultipart()
    msg['From'] = formataddr(('Sender', from_email))
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, 'aqsodnlcfdasxgux')
        server.sendmail(from_email, to_email, msg.as_string())
        logging.info('Email sent successfully')
        server.quit()
        
        
    except Exception as e:
        logging.error(f'Error sending email: {str(e)}')
        raise HTTPException(status_code=500, detail='Failed to send email')

@app.post('/send_email')
def send_email_route(email: Email):
    if not re.match(EMAIL_REGEX, email.to):

        logging.warning('Invalid email format:')
        raise HTTPException(status_code=422, detail='Invalid email format')
    send_email(email)
    logging.info(f'Email sent to: {email.to}')
    return {'message': 'Email sent'}

