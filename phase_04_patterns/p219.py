class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.observers = []
    
    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def deposit(self, amount):
        self.balance += amount
        self.notify(f"Deposited {amount}, new balance : {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.notify(f"Withdrew {amount}, new balance : {self.balance}")
        else:
            self.notify("Insufficient funds")

class EmailNotifier:
    def __init__(self, email):
        self.email = email

    def update(self, message):
        print(f"Email to {self.email}: {message}")

class SmsNotifier:
    def __init__(self, phone):
        self.phone = phone

    def update(self, message):
        print(f"SMS to {self.phone}: {message}")

class PushNotifier:
    def __init__(self, device):
        self.device = device

    def update(self, message):
        print(f"Push notification to {self.device}: {message}")

account = BankAccount(1000)

account.attach(EmailNotifier("user@gmail.com"))
account.attach(SmsNotifier("+1-234-567-8901"))
account.attach(PushNotifier("device123"))  

account.deposit(500)
account.withdraw(200)