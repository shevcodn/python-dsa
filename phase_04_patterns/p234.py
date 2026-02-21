class PaymentStrategy:
    def pay(self, amount):
        self.amount = amount

class CreditCardPayment(PaymentStrategy):
    def __init__(self, account):
        self.account = account

    def pay(self, amount):
        super().pay(amount)
        print(f"Paid {self.amount} using CreditCard: {self.account}")

class PayPalPayment(PaymentStrategy):
    def __init__(self, account):
        self.account = account

    def pay(self, amount):
        super().pay(amount)
        print(f"Paid {self.amount} using PayPal: {self.account}")

class BitcoinPayment(PaymentStrategy):
    def __init__(self, account):
        self.account = account

    def pay(self, amount):
        super().pay(amount)
        print(f"Paid {self.amount} using Bitcoin: {self.account}")

class ShoppingCart:
    def __init__(self):
        self.payment_method = None

    def set_payment_strategy(self, strategy):
        self.payment_method = strategy

    def checkout(self, amount):
        self.payment_method.pay(amount)

cart = ShoppingCart()

cart.set_payment_strategy(CreditCardPayment("1234-5678"))
cart.checkout(100)

cart.set_payment_strategy(PayPalPayment("email@gmail.com"))
cart.checkout(50)

cart.set_payment_strategy(BitcoinPayment("0xABC123"))
cart.checkout(200)