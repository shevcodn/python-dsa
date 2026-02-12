class TrafficLight:
    def __init__(self):
        self.state = "red"

    def change(self):
        if self.state == "red":
            self.state = "green"
        elif self.state == "green":
            self.state = "yellow"
        elif self.state == "yellow":
            self.state = "red"

    def display(self):
        print(f"Traffic light is {self.state}")

light = TrafficLight()
light.display()
light.change()
light.display()
light.change()
light.display() 
light.change()
light.display()