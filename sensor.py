from typing import Self


class Sensor:
    def __init__(self: Self, zombie: bool) -> None:
        self._state: bool = zombie

    def get_state(self: Self) -> bool:
        return self._state

    def set_state(self: Self, zombie: bool) -> None:
        self._state = zombie

    def print(self: Self) -> str:
        return "Zombies!" if self._state else " "
