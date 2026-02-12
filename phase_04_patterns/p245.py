class ChatRoom:
    def __init__(self):
        self.users = []

    def send_message(self, message, from_user):
        print(f"{from_user.name}: {message}")
        for user in self.users:
            if user != from_user:
                user.receive(message)

    def add_user(self, user):
        self.users.append(user)

class User:
    def __init__(self, name, chat_room):
        self.name = name
        self.chat_room = chat_room
        self.chat_room.users.append(self)

    def send(self, message):
        self.chat_room.send_message(message, self)

    def receive(self, message):
        print(f"{self.name} received: {message}")

chatroom = ChatRoom()

alice = User("Alice", chatroom)
bob = User("Bob", chatroom)

alice.send("Hello, Bob!")

