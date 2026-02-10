class LoggedTransaction:
    def __init__(self, transaction):
        self.transaction = transaction
    
    def execute(self):
        print("[LOG] Transaction started")
        self.transaction.execute()
        print("[LOG] Transaction completed")

class ValidatedTransaction:
    def __init__(self, transaction, amount):
        self.transaction = transaction
        self.amount = amount

    def execute(self):
        if self.amount > 0:
            print("[VALIDATION] Amount is valid")
            self.transcation.execute()
        elif self.amount <= 0:
            print("[VALIDATION] Invalid Amount")
    
class Transaction:
    def execute(self):
        print("Executing transaction")

t1 = Transaction()
t1.execute()

t2 = LoggedTransaction(t1)
t2.execute()

t3 = LoggedTransaction(ValidatedTransaction(t1, 100))
t3.execute

t4 = ValidatedTransaction(t1, -50)
t4.execute()


