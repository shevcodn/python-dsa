class SupportHandler:
    def __init__(self):
        self.next_handler = None
    
    def set_next(self, handler):
        self.next_handler = handler
        return handler
    
    def handle(self, ticket):
        if self.next_handler:
            return self.next_handler.handle(ticket)
        return None
    
class Level1Support(SupportHandler):
    def handle(self, ticket):
        if ticket == "basic":
            print("Level 1: Handled basic issue")
        else:
            return super().handle(ticket)
        
class Level2Support(SupportHandler):
    def handle(self, ticket):
        if ticket == "intermediate":
            print("Level 2: Handled intermediate issue")
        else:
            return super().handle(ticket)
        
class Level3Support(SupportHandler):
    def handle(self, ticket):
        if ticket == "advanced":
            print("Level 3: Handled advanced issue")
        else:
            return super().handle(ticket)
        
level1 = Level1Support()
level2 = Level2Support()
level3 = Level3Support()

level1.set_next(level2).set_next(level3)

level1.handle("basic")
level1.handle("intermediate")
level1.handle("advanced")

