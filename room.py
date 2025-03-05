from sensor import Sensor
from typing import Self


class Room:
    """Clase que representa un piso dentro del edificio, y el sensor dentro de este."""

    def __init__(self: Self, floor: int, room_number: int, zombie: bool) -> None:
        """Inicializa el cuarto y el sensor de este, con el estado de zombie determinado por el piso."""
        self.floor: int = floor
        self.room_number: str = f"{floor+1}0{room_number}"
        self._sensor = Sensor(zombie)

    def get_sensor(self: Self) -> bool:
        """Retorna el estado del sensor."""
        return self._sensor.get_state()

    def set_sensor(self: Self, zombie: bool) -> None:
        """Cambia el estado del sensor al estado recibido."""
        self._sensor.set_state(zombie)

    def print(self: Self) -> str:
        """Retorna la representacion visual del sensor dentro del piso."""
        return self._sensor.print()
