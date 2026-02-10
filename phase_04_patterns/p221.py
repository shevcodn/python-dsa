class StripeAPI:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def charge_card(self, amount):
        print(f"Stripe: Charged ${amount} processed")

class PayPalAPI:
    def __init__(self, email):
        self.email = email

    def make_payment(self, amount):
        print(f"Paypal: Payment ${amount} processed")

class PayPalAdapter:
    def __init__(self, paypal_api):
        self.paypal_api = paypal_api
    
    def charge_card(self, amount):
        self.paypal_api.make_payment(amount)

stripe = StripeAPI("sk_test_123")
stripe.charge_card(100)

paypal = PayPalAdapter(PayPalAPI("client@gmail.com"))
paypal.charge_card(200)