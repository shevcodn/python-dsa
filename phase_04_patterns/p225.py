class CreditCardPayment:
    def process(self, amount):
        return f"Processed ${amount} via Credit Card"
    
class PayPalPayment:
    def process(self, amount):
        return f"Processed ${amount} via PayPal"
    
class TransactionLogger:
    def update(self, message):
        print(f"[LOG] {message}")

class FraudChecker:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process(self, amount):
        if amount > 10000:
            return "FRAUD: Amount too high!"
        else:
            return self.payment_method.process(amount)
        
class StripeAPI:
    def charge(self, amount):
        return f"Stripe charged ${amount}"
    
class StripeAdapter:
    def __init__(self):
        self.stripe = StripeAPI()

    def process(self, amount):
        return self.stripe.charge(amount)
    
class PaymentProcessor:
    def __init__(self):
        self.logger = TransactionLogger()
        self.payment_method = None
    
    def set_payment_method(self, method):
        self.payment_method = method

    def process_payment(self, amount):
        self.logger.update(f"Processing payment of ${amount}")
        result = self.payment_method.process(amount)
        self.logger.update(f"Result: {result}")
        return result
    

processor = PaymentProcessor()

credit_card = CreditCardPayment()
fraud_checker = FraudChecker(credit_card)
processor.set_payment_method(fraud_checker)
print(processor.process_payment(5000))

print(processor.process_payment(15000))

stripe = StripeAdapter()
processor.set_payment_method(stripe)
print(processor.process_payment(2000))
