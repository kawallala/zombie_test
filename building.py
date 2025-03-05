from floor import Floor
from room import Room
from typing import Self


class Building:
    def __init__(self: Self, num_floors: int, rooms_per_floor: int) -> None:
        self.num_floors: int = num_floors
        self.rooms_per_floor: int = rooms_per_floor
        self._floors: list[Floor] = []
        for i in range(num_floors):
            self._floors.append(Floor(i, rooms_per_floor))

    def get(self: Self, floor: int, room: int) -> Room:
        rooms_of_floor = self._floors[floor].get_rooms()
        return rooms_of_floor[room]

    def set(self: Self, floor: int, room: int, zombie: bool) -> None:
        self._floors[floor].set_room_sensor(room, zombie)

    def advance(self: Self) -> None:
        directions: list[tuple[int, int]] = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]
        new_zombies: list[tuple[int, int]] = []
        for f, floor in enumerate(self._floors):
            for r, room in enumerate(floor.get_rooms()):
                if room.get_sensor() and (f, r) not in new_zombies:
                    print(f"Zombie en cuarto {room.room_number}")
                    for dx, dy in directions:
                        fn = f + dx
                        rn = r + dy
                        if 0 <= fn < self.num_floors and 0 <= rn < self.rooms_per_floor:
                            self.set(fn, rn, True)
                            new_zombies.append((fn, rn))

    def print(self: Self) -> None:
        for i, floor in enumerate(self._floors):
            print(f"Piso {i+1}".rjust(30, "-").ljust(40, "-"))
            floor.print()
