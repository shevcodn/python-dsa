class EmailValidator:
    def validate(self, email):
        if "@" in email and "." in email:
            return True
        else:
            return False
        
class UserDatabase:
    def save(self, name):
        print(f"Saving {name} to database...")
        return True
    
class EmailService:
    def send_welcome(self, email):
        print(f"Sending welcome email to {email}")
        return True
    
class UserManager:
    def __init__(self):
        self.validator = EmailValidator()
        self.database = UserDatabase()
        self.email_service = EmailService()

    def create_user(self, name, email):
        if not self.validator.validate(email):
            print("Invalid email")
            return False
        
        self.database.save(name)
        self.email_service.send_welcome(email)
        return True
    
manager = UserManager()
print(manager.create_user("John", "john@email.com"))
print(manager.create_user("Bob", "bobemail.com"))