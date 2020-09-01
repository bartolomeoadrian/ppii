import productos


def iniciar():
    """
    Inicia el menu de acciones del supermercado

    :return: None
    """
    while True:
        print("1) Buscar producto")
        print("2) Ingresar nueva factura")
        print("3) Ingresar nuevo producto")
        print("4) Salir")

        print("\nPor favor, seleccione la opcion:")

        opcion = input()

        if opcion == "1":
            buscar_producto()
        elif opcion == "2":
            ingresar_factura()
        elif opcion == "3":
            ingresar_producto()
        elif opcion == "4":
            break;
        else:
            print("No ha ingresado una opcion válida")


def buscar_producto():
    codigo = None

    while True:
        codigo = input("Ingrese el código del producto: ")
        if not codigo.isdigit():
            print("Por favor, ingrese un número")
        else:
            codigo = int(codigo)
            break

    producto = productos.buscar(codigo)

    if producto:
        print(f"Se encontró un producto con el código {codigo}")
        print(producto)
    else:
        print(f"No se encontró un producto con el código {codigo}")


def ingresar_factura():
    return None


def ingresar_producto():
    return None
