class Sensor:
    def __init__(self) -> None:
        self.state: bool = False

    def print(self):
        return "Zombies!" if self.state else " "
