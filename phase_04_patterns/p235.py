class Light:
    def turn_on(self):
        print("Light turned on")

    def turn_off(self):
        print("Light turned off")

class TurnOnCommand:
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

class TurnOffCommand:
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

class RemoteControl:
    def __init__(self):
        self.light = None

    def execute_command(self, command):
        command.execute()
        self.last_command = command

    def undo(self):
        if self.last_command:
            self.last_command.undo()

light = Light()
remote = RemoteControl()

on_cmd = TurnOnCommand(light)
off_cmd = TurnOffCommand(light)

remote.execute_command(on_cmd)
remote.execute_command(off_cmd)

remote.undo()