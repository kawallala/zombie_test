from sensor import Sensor
from typing import Self


class Room:
    def __init__(self: Self, floor: int, room_number: int, zombie: bool) -> None:
        self.floor: int = floor
        self.room_number: str = f"{floor+1}0{room_number}"
        self._sensor = Sensor(zombie)

    def get_sensor(self: Self) -> bool:
        return self._sensor.get_state()

    def set_sensor(self: Self, zombie: bool) -> None:
        self._sensor.set_state(zombie)

    def print(self: Self) -> str:
        return self._sensor.print()
