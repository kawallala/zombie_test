def main():
    print("Bienvenido a esta simulacion de un edificio infectado por zombies, tu objetivo es evitar inunden todos los cuartos")
    print("Pero primero, configuremos el edificio")
    floors = input("Cuantos pisos tendra tu edificio? ")
    rooms_per_floor = input("Cuantas habitaciones habran por piso? ")
    print(floors)
    print(rooms_per_floor)
    # building = Building(floors, rooms_per_floor)

    #Main loop
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
                print(1)
            case 2:
                print(2)
            case 99:
                return
            case default:
                print("Opcion no disponible, intenta otra vez")


if __name__ == "__main__":
    main()
