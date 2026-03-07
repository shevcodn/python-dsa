from typing import Protocol

class Notifiable(Protocol):
    def notify(self, message: str) -> None:
        ...

class Saveable(Protocol):
    def save(self) -> bool:
        ...

class EmailNotifier:
    def notify(self, message: str) -> None:
        print(f"Email notification: {message}")

class SMSNotifier:
    def notify(self, message: str) -> None:
        print(f"SMS notification: {message}")

def send_alert(notifier: Notifiable, message: str) -> None:
    notifier.notify(message)

email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()
send_alert(email_notifier, "This is an email alert!")
send_alert(sms_notifier, "This is an SMS alert!")

