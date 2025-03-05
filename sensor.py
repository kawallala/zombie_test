from typing import Self


class Sensor:
    """Clase que representa un sensor."""

    def __init__(self: Self, zombie: bool) -> None:
        """Inicializa el sensor con el estado entregado."""
        self._state: bool = zombie

    def get_state(self: Self) -> bool:
        """Retorna el estado del sensor."""
        return self._state

    def set_state(self: Self, zombie: bool) -> None:
        """Cambia el estado del sensor al estado entregado."""
        self._state = zombie

    def print(self: Self) -> str:
        """Retorna la representacion visual del estado del sensor."""
        return "Zombies!" if self._state else " "
