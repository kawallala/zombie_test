from room import Room
from typing import Self
import random


class Floor:
    """Clase que representa un piso y sus cuartos."""

    def __init__(self: Self, floor_number: int, rooms_per_floor: int) -> None:
        """Inicializa el piso y los cuartos dentro de este, determinando si estos poseen un zombie."""
        self._rooms: list[Room] = []
        self._floor_number: int = floor_number
        for i in range(rooms_per_floor):
            zombie = False
            if random.randrange(0, 100) < 10:
                zombie = True
            self._rooms.append(Room(floor_number, i, zombie))

    def get_floor_number(self: Self) -> int:
        """Retorna el numero del piso."""
        return self._floor_number

    def get_rooms(self: Self) -> list[Room]:
        """Retorna la lista de cuartos dentro del piso."""
        return self._rooms

    def set_room_sensor(self: Self, room: int, zombie: bool) -> None:
        """Cambia el estado de un sensor dentro de un cuarto específico."""
        self._rooms[room].set_sensor(zombie)

    def print(self: Self) -> None:
        """Retorna la representacion visual del piso, y los cuartos dentro de este."""
        str_top = ""
        str_middle = ""
        str_bottom = ""
        for room in self._rooms:
            room_state = room.print()
            str_top += "|" + f"{room.room_number}".center(18, "=") + "|"
            str_middle += "|" + f"{room_state}".center(18, " ") + "|"
            str_bottom += "|" + "=" * 18 + "|"
        print(str_top)
        print(str_middle)
        print(str_bottom)
