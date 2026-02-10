class FraudDetectionService:
    def check_fraud(self, amount, account):
        print("[FRAUD] Checking transaction...")
        return True
    
class PaymentGateway:
    def process_payment(self, amount):
        print(f"[GATEWAY] Processing ${amount}")
        return True
    
class NotificationService:
    def send_receipt(self, email, amount):
        print(f"[EMAIL] Receipt sent to {email} for ${amount}")

class TransactionLogger:
    def log_transaction(self, amount, status):
        print(f"[LOG] Transaction ${amount}: {status}")

class PaymentFacade:
    def __init__(self):
        self.fraud_service = FraudDetectionService()
        self.gateway = PaymentGateway()
        self.notifier = NotificationService()
        self.logger = TransactionLogger()

    def make_payment(self, amount, email, account):
        if self.fraud_service.check_fraud(amount, account):
            if self.gateway.process_payment(amount):
                self.notifier.send_receipt(email, amount)
                self.logger.log_transaction(amount, "Success")
            else:
                self.logger.log_transaction(amount, "Failed at gateway")
        else:
            self.logger.log_transaction(amount, "Failed fraud check")

fraud = FraudDetectionService()
gateway = PaymentGateway()
notifier = NotificationService()
logger = TransactionLogger()

if fraud.check_fraud(100, "acc123"):
    if gateway.process_payment(100):
        notifier.send_receipt("user@gmail.com", 100)
        logger.log_transaction(100, "Success")
        print("Payment Successful!")
    else:
        logger.log_transaction(100, "Failed at gateway")
else:
    logger.log_transaction(100, "Failed fraud check")
