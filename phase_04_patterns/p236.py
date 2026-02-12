class Coffee:
    def __init__(self):
        pass

    def cost(self):
        return 5
    
    def description(self):
        return "Coffee"
    
class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 2
    
    def description(self):
        return self.coffee.description() + " Milk"

class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 1
    
    def description(self):
        return self.coffee.description() + " Sugar"

coffee = Coffee()
print(coffee.cost())
print(coffee.description())

coffee_with_milk = MilkDecorator(coffee)
print(coffee_with_milk.cost())
print(coffee_with_milk.description())

coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print(coffee_with_milk_and_sugar.cost())
print(coffee_with_milk_and_sugar.description())