from sensor import Sensor


class Room:
    def __init__(self, floor: int, room_number: int, zombie: bool) -> None:
        self.floor = floor
        self.room_number = f"{floor}0{room_number}"
        self.sensor = Sensor()

    def print(self):
        return self.sensor.print()
