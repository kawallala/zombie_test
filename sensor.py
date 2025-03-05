class Sensor:
    def __init__(self, zombie: bool) -> None:
        self.state: bool = zombie

    def print(self):
        return "Zombies!" if self.state else " "
