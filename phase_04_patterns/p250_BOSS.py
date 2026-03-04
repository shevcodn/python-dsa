class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'orders'):
            self.orders = {}

    def add_order(self, order):
        self.orders[order.order_id] = order
    
    def get_order(self, order_id):
        return self.orders.get(order_id)
    
class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
        self.state = "pending"
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def calculate_shipping(self):
        return 0
    
class StandardOrder(Order):
    def calculate_shipping(self):
        return 10
        
class ExpressOrder(Order):
    def calculate_shipping(self):
        return 25
    
class OrderFactory:
    @staticmethod
    def create_order(order_type, order_id, items):
        if order_type == "standard":
            return StandardOrder(order_id, items)
        elif order_type == "express":
            return ExpressOrder(order_id, items)
        else:
            raise ValueError("Unknown order type")
        
class EmailNotifier:
    def __init__(self, email):
        self.email = email

    def update(self, order):
        print(f"Email to {self.email}: Order {order.order_id} is now {order.state}")

class SMSNotifier:
    def __init__(self, phone):
        self.phone = phone

    def update(self, order):
        print(f"SMS to {self.phone}: Order {order.order_id} is now {order.state}")

class OrderStateMachine:
    def __init__(self, order):
        self.order = order

    def next_state(self):
        states = ["pending", "processing", "shipped", "delivered"]
        idx = states.index(self.order.state)
        if idx < len(states) - 1:
            self.order.state = states[idx + 1]
            self.order.notify()

db = Database()
order = OrderFactory.create_order("express", "12345", ["item1", "item2"])

email = EmailNotifier("denis@gmail.com")
order.attach(email)

db.add_order(order)

state = OrderStateMachine(order)
state.next_state()
print(order.calculate_shipping())