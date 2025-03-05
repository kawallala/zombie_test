from sensor import Sensor


class Room:
    def __init__(self, floor: int, room_number: int, zombie: bool) -> None:
        self.floor: int = floor
        self.room_number: str = f"{floor+1}0{room_number}"
        self.sensor = Sensor(zombie)

    def get_sensor(self) -> bool:
        return self.sensor.state

    def set_sensor(self, zombie: bool) -> None:
        self.sensor.state = zombie

    def print(self):
        return self.sensor.print()
