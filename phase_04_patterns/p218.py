class CreditCardPayment:
    def __init__(self, account):
        self.account = account

    def pay(self, amount):
        print(f"Paid {amount} using CreditCard: {self.account}")

class PayPalPayment:
    def __init__(self, account):
        self.account = account

    def pay(self, amount):
        print(f"Paid {amount} using PayPal: {self.account}")

class CryptoPayment:
    def __init__(self, account):
        self.account = account

    def pay(self, amount):
        print(f"Paid {amount} using Crypto: {self.account}")

class ShoppingCart:
    def __init__(self):
        self.payment_method = None

    def set_payment(self, payment_method):
        self.payment_method = payment_method

    def checkout(self, amount):
        self.payment_method.pay(amount)

cart = ShoppingCart()

cart.set_payment(CreditCardPayment("1234-5678"))
cart.checkout(100)

cart.set_payment(PayPalPayment("user@gmail.com"))
cart.checkout(200)

cart.set_payment(CryptoPayment("0xABC123"))
cart.checkout(300)