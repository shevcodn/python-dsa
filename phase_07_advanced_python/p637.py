class Order:
    def __init__(self, items, user_email):
        self.items = items
        self.user_email = user_email

    def calculate_total(self):
        return sum(i["price"] for i in self.items)


class EmailService:
    def send_confirmation(self, email, order):
        print(f"Email sent to {email}: order confirmed")


class OrderRepository:
    def save(self, order):
        print(f"Order saved: {order.items}")


order = Order([{"price": 100}, {"price": 50}], "denis@test.com")
email_service = EmailService()
repo = OrderRepository()

print(order.calculate_total())
email_service.send_confirmation(order.user_email, order)
repo.save(order)
