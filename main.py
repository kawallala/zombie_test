from building import Building


def main():
    print("Bienvenido a esta simulacion de un edificio infectado por zombies")
    print("Primero, configuremos el edificio")
    while True:
        try:
            floors = int(input("Cuantos pisos tendra tu edificio? "))
            break
        except:
            print("por favor ingresa un numero")
    while True:
        try:
            rooms_per_floor = int(input("Cuantas habitaciones habran por piso? "))
            break
        except:
            print("Por favor ingresa un numero")
    building = Building(floors, rooms_per_floor)

    # Main loop
    while True:
        print("Que vas a hacer? \n")
        print("1- Ver estado edificio")
        print("2- Avanzar simulacion")
        print("99- Salir")
        try:
            option = int(input())
        except:
            option = None
        match option:
            case 1:
                print("Estado edificio")
                building.print()
            case 2:
                print("Avanzando simulacion")
                building.advance()
            case 99:
                return
            case default:
                print("Opcion no disponible, intenta otra vez")


if __name__ == "__main__":
    main()
