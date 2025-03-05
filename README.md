# Instalacion

Basta con clonar el repositorio, luego acceder a la carpeta de este y ejecutar el programa mediante la instalacion de python en la maquina.

```
git clone https://github.com/kawallala/zombie_test
cd zombie_test/
python3 main.py
```

# Arquitectura

El código se basa en 1 clase principal `main.py` que se encarga de la ejecución de la simulación y la interacción con el usuario, y 4 clases que representan las distintas partes del edificio.

- `building.py` Representación del edificio
- `floor.py` Representación de un piso del edificio
- `room.py` Representación de un cuarto del edificio
- `sensor.py` Representación de un sensor dentro de un cuarto

# Acciones

Al ejecutar el programa este muestra la lista de acciones posibles, estas se detallan a continuación

- Visualizar el estado del edificio
- Avanzar la simulación

La simulación esta configurada para que los zombies se expandan de forma incontrolable, expandiendose a todos los cuartos adyacentes.

# Posibles mejoras

A continuación se detalla una lista de mejoras posibles para el programa

- Indicar la posición de un jugador
- Bloquear un cuarto
- Determinar de forma aleatoria la expansión de zombies
