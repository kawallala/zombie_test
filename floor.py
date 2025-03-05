from room import Room
from typing import Self
import random


class Floor:
    def __init__(self: Self, floor_number: int, rooms_per_floor: int) -> None:
        self._rooms: list[Room] = []
        self.floor_number: int = floor_number
        for i in range(rooms_per_floor):
            zombie = False
            if random.randrange(0, 100) < 10:
                zombie = True
            self._rooms.append(Room(floor_number, i, zombie))

    def get_rooms(self: Self) -> list[Room]:
        return self._rooms

    def set_room_sensor(self: Self, room: int, zombie: bool) -> None:
        self._rooms[room].set_sensor(zombie)

    def print(self: Self) -> None:
        str_top = ""
        str_middle = ""
        str_bottom = ""
        for room in self._rooms:
            room_state = room.print()
            str_top += f"{room.room_number}".rjust(10, "=").ljust(20, "=")
            str_middle += f"{room_state[0]}".rjust(10, " ").ljust(20, " ")
            str_bottom += "=".rjust(10, "=").ljust(20, "=")
        print(str_top)
        print(str_middle)
        print(str_bottom)
