import pytest
from unittest.mock import Mock

class EmailService:
    def __init__(self, smtp):
        self.smtp = smtp
        self.sent = []

    def send(self, to, subject, body):
        self.smtp.send_mail(to, subject, body)
        self.sent.append(({"to": to, "subject": subject, "body": body}))
        return True
    
@pytest.fixture
def smtp():
    return Mock()

@pytest.fixture
def email_service(smtp):
    return EmailService(smtp)

def test_send_email(email_service, smtp):
    result = email_service.send("denis@test.com", "Hello", "Body")
    assert result is True
    assert len(email_service.sent) == 1
    smtp.send_mail.assert_called_once_with("denis@test.com", "Hello", "Body")

def test_send_multiple(email_service):
    email_service.send("a@test.com", "S1", "B1")
    email_service.send("b@test.com", "S2", "B2")
    assert len(email_service.sent) == 2

