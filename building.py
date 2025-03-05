from floor import Floor


class Building:
    def __init__(self, num_floors: int, rooms_per_floor: int) -> None:
        self.num_floors = num_floors
        self.rooms_per_floor = rooms_per_floor
        self.floors = []
        for i in range(num_floors):
            self.floors.append(Floor(i, rooms_per_floor))

    def advance(self):
        for floor in self.floors:
            floor.advance()

    def print(self):
        for i, floor in enumerate(self.floors):
            print(f"Piso {i+1}".rjust(30, "-").ljust(40, "-"))
            floor.print()
