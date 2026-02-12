class NewsPublisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, news):
        for subscriber in self.subscribers:
            subscriber.update(news)

class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} received: {news}")

publisher = NewsPublisher()

alice = Subscriber("Alice")
bob = Subscriber("Bob")

publisher.subscribe(alice)
publisher.subscribe(bob)

publisher.notify("Breaking news!")

publisher.unsubscribe(alice)
publisher.notify("Update")

