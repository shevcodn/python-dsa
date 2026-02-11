class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")        

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processed ${amount} via Stripe")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processed ${amount} via PayPal")

class BitcoinProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processed ${amount} via Bitcoin")

class PaymentProcessorFactory:
    def create_processor(self, payment_type):
        if payment_type == "stripe":
            return StripeProcessor()
        elif payment_type == "paypal":
            return PayPalProcessor()
        elif payment_type == "bitcoin":
            return BitcoinProcessor()
        else:
            raise ValueError("Unknown payment type")
        

factory = PaymentProcessorFactory()

stripe = factory.create_processor("stripe")
stripe.process_payment(100)

paypal = factory.create_processor("paypal")
paypal.process_payment(50)

bitcoin = factory.create_processor("bitcoin")
bitcoin.process_payment(200)

unknown = factory.create_processor("unknown")