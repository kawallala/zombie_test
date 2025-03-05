from floor import Floor
from room import Room
from typing import Self


class Building:
    """Clase que representa un edificio y sus funciones, guarda un registro de los pisos dentro de este."""

    def __init__(self: Self, num_floors: int, rooms_per_floor: int) -> None:
        """Inicializa la clase Building, crea todos los pisos y les entrega la cantidad de cuartos en cada uno."""
        self.num_floors: int = num_floors
        self.rooms_per_floor: int = rooms_per_floor
        self._floors: list[Floor] = []
        for i in range(num_floors):
            self._floors.append(Floor(i, rooms_per_floor))

    def get(self: Self, floor: int, room: int) -> Room:
        """Retorna un cuarto especifico, dado un piso y numero de cuarto."""
        rooms_of_floor = self._floors[floor].get_rooms()
        return rooms_of_floor[room]

    def set(self: Self, floor: int, room: int, zombie: bool) -> None:
        """Setea el estado de un sensor dentro de un cuarto."""
        self._floors[floor].set_room_sensor(room, zombie)

    def advance(self: Self) -> None:
        """
        Avanza la simulacion un paso, tomando la lista de pisos y expandiendo los zombies.

        Por cada piso, se toma cada cuarto y se evalua si este posee un zombie.
        En caso de no poseer un zombie, se cambia el estado del cuarto correspondiente.
        Se utiliza la lista new_zombies para almacenar los cuartos donde se han cambiado el estado en la iteracion
        actual, para evitar expandir recursivamente.
        """
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
        """Retorna la representacion visual del edificio y sus pisos."""
        length = self.rooms_per_floor * 20
        reversed = self._floors
        reversed.reverse()
        for _, floor in enumerate(reversed):
            print(f"Piso {floor.get_floor_number()}".center(length, "="))
            floor.print()
