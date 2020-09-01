import math


def ingresar_coordenadas():
    """
    Permite que el usuario ingrese coordenadas x,y y se devuelva la distancia al origen. Se ingresa 0,0 para finalizar

    :return: None
    """
    while True:
        entrada = input("Por favor, ingrese el punto en formato x,y: ")
        coords = entrada.split(",")

        if len(coords) != 2:
            print("El formato de datos es incorrecto")
        else:
            x = coords[0].strip()
            y = coords[1].strip()

            if not x.isdigit() or not y.isdigit():
                print("Por favor, ingrese solo numeros")
            else:
                distancia = calcular_distancia(int(x), int(y))

                print(f"La distancia al origen del punto ({x},{y}) es: {str(distancia)}")

                if x == "0" and y == "0":
                    break

    print("Programa finalizado")


def calcular_distancia(x, y):
    """
    Calcula la distancia al origen de un punto en el plano

    :param x: int - punto x
    :param y: int - punto y
    :return: int - distancia del punto al origen
    """
    return math.sqrt((x*x) + (y*y))
