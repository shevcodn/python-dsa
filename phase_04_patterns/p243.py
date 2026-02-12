class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def boil_water(self):
        print("Boiling water")

    def brew(self):
        print(f"Brewing {self.name}")

    def pour(self):
        print(f"Pouring {self.name} into cup")

    def add_condiments(self):
        print(f"Adding condiments to {self.name}")

    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour()
        self.add_condiments()

class Tea(Beverage):
    def __init__(self):
        super().__init__("Tea", 1.5)

    def brew(self):
        print("Steeping tea leaves")

    def add_condiments(self):
        print("Adding lemon")

class Coffee(Beverage):
    def __init__(self):
        super().__init__("Coffee", 2.0)

    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")

tea = Tea()
tea.prepare()

coffee = Coffee()
coffee.prepare()