class SupportHandler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler
    
    def handle(self, issue):
        if self.next_handler:
            return self.next_handler.handle(issue)

class Level1Support(SupportHandler):
    def handle(self, request):
        if request == "password reset":
            print ("Level 1: Password reset handled")
        else:
            return super().handle(request)
        
class Level2Support(SupportHandler):
    def handle(self, request):
        if request == "bug report":
            print ("Level 2: Bug report handled")
        else:
            return super().handle(request)
        
class Level3Support(SupportHandler):
    def handle(self, request):
        if request == "feature request":
            print ("Level 3: Feature request handled")
        else:
            print (f"Cannot handle: {request}")
        
level1 = Level1Support()
level2 = Level2Support()
level3 = Level3Support()

level1.set_next(level2)
level2.set_next(level3)

level1.handle("password reset")
level1.handle("bug report")
level1.handle("feature request")
level1.handle("unknown")