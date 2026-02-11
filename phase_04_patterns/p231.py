class VendingMachine:
    def __init__(self):
        self.state = "idle"

    def insert_money(self):
        if self.state == "idle":
            print("Money inserted")
            self.state = "has_money"

    def select_item(self):
        if self.state == "has_money":
            print("Item selected")
            self.state = "dispensing"

    def dispense(self):
        if self.state == "dispensing":
            print("Dispensing item")
            self.state = "idle"

machine = VendingMachine()

machine.insert_money()
machine.select_item()
machine.dispense()