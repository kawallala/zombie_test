from sensor import Sensor


class Room:
    def __init__(self, floor: int, room_number: int, zombie: bool) -> None:
        self.floor: int = floor
        self.room_number: str = f"{floor+1}0{room_number}"
        self._sensor = Sensor(zombie)

    def get_sensor(self) -> bool:
        return self._sensor.state

    def set_sensor(self, zombie: bool) -> None:
        self._sensor.state = zombie

    def print(self):
        return self._sensor.print()
