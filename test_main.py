from fastapi.testclient import TestClient
from main import app
import pytest
import logging

client = TestClient(app)


def test_send_email(caplog):
    email_data = {
        'to': 'nurbekakbolat8@gmail.com',
        'subject': 'Test email',
        'message': 'This is a test email. Success'
    }
    
    
    with caplog.at_level(logging.INFO):
        response = client.post('/send_email', json=email_data)
    for record in caplog.records:
        if record.message == "Email sent successfully":
            assert True
            break
    

    
    

def test_send_email_invalid(caplog):
    email_data = {
        'to': 'invalid_email',
        'subject': 'Test email',
        'message': 'Error'
    }
    with caplog.at_level(logging.INFO):
        response = client.post('/send_email', json=email_data)

    assert response.status_code == 422








 
