import pytest                                                    

class BankAccount:                                               
    def __init__(self, owner, balance=0):                        
        self.owner = owner                                       
        self.balance = balance                                   
        self.history = []                                        
                                                                   
    def deposit(self, amount):                                   
        self.balance += amount
        self.history.append(f"+{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.history.append(f"-{amount}")


@pytest.fixture
def account():
    return BankAccount("Denis", 1000)


def test_deposit(account):
    account.deposit(200)
    assert account.balance == 1200


def test_withdraw(account):
    account.withdraw(100)
    assert account.balance == 900


def test_withdraw_overdraft(account):
    with pytest.raises(ValueError) as exc:
        account.withdraw(1500)
    

def test_history(account):
    account.deposit(100)
    account.withdraw(50)
    assert len(account.history) == 2
    
