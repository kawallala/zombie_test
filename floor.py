from room import Room
import random


class Floor:
    def __init__(self, floor_number: int, rooms_per_floor: int) -> None:
        self.rooms = []
        self.floor_number = floor_number
        for i in range(rooms_per_floor):
            zombie = random.choice([True, False])
            self.rooms.append(Room(floor_number, i, zombie))

    def print(self):
        str_top = ""
        str_middle = ""
        str_bottom = ""
        for room in self.rooms:
            room_state = room.print()
            str_top += f"{room.room_number}".rjust(10, "=").ljust(20, "=")
            str_middle += f"{room_state[0]}".rjust(10, " ").ljust(20, " ")
            str_bottom += "=".rjust(10, "=").ljust(20, "=")
        print(str_top)
        print(str_middle)
        print(str_bottom)
