class EmailSender:
    def send_message(self, message):
        print(f"EMAIL: {message}")

class SMSSender:
    def send_message(self, message):
        print(f"SMS: {message}")

class Notification:
    def __init__(self, sender):
        self.sender = sender

    def notify(self, message):
        self.sender.send_message(message)

class UrgentNotification(Notification):
    def notify(self, message):
        self.sender.send_message(f"[URGENT]: {message}")

class RegularNotification(Notification):
    def notify(self, message):
        self.sender.send_message(f"[REGULAR]: {message}")

email = EmailSender()
sms = SMSSender()

urgent_email = UrgentNotification(email)
urgent_email.notify("Server down!")

regular_sms = RegularNotification(sms)
regular_sms.notify("Daily report ready.")

