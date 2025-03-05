from floor import Floor


class Building:
    def __init__(self, num_floors: int, rooms_per_floor: int) -> None:
        self.num_floors: int = num_floors
        self.rooms_per_floor: int = rooms_per_floor
        self._floors: list[Floor] = []
        for i in range(num_floors):
            self._floors.append(Floor(i, rooms_per_floor))

    def get(self, floor: int, room: int):
        return self._floors[floor]._rooms[room]

    def set(self, floor: int, room: int, zombie: bool):
        self._floors[floor].set_room_sensor(room, zombie)

    def advance(self):
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]
        new_zombies = []
        for f, floor in enumerate(self._floors):
            for r, room in enumerate(floor._rooms):
                if room.get_sensor() and (f, r) not in new_zombies:
                    print(f"Zombie en cuarto {room.room_number}")
                    for dx, dy in directions:
                        fn = f + dx
                        rn = r + dy
                        if 0 <= fn < self.num_floors and 0 <= rn < self.rooms_per_floor:
                            self.set(fn, rn, True)
                            new_zombies.append((fn, rn))

    def print(self):
        for i, floor in enumerate(self._floors):
            print(f"Piso {i+1}".rjust(30, "-").ljust(40, "-"))
            floor.print()
