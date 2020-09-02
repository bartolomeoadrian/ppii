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
            break
        else:
            print("No ha ingresado una opcion válida")


def buscar_producto():
    """
    Ingresando el codigo de un producto lo busca en el catalogo y lo informa por pantalla

    :return: None
    """
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
    """
    Permite al usuario buscar varios productos para crear una factura con ellos con su respectiva cantidad
    e indicar el total a pagar. Ingrese codigo de producto 'F' para terminar

    :return: None
    """
    factura = []
    total = 0

    while True:
        codigo = input("Ingrese el codigo del producto: ")

        if codigo == "F":
            break

        if not codigo.isdigit():
            print("El codigo que ingresó no es un número, intentelo nuevamente")
            continue

        producto = productos.buscar(int(codigo))

        if not producto:
            print("No existe un producto con ese codigo")
            continue

        cantidad = input("Ingrese la cantidad a solicitar: ")

        if not cantidad.isdigit():
            print("La cantidad que ingresó no es un número, intentelo nuevamente")
            continue

        factura.append({'producto': producto, 'cantidad': int(cantidad)})
        total += int(cantidad) * producto['precio']

    print(factura)
    print(f"Total: ${total}")


def ingresar_producto():
    """
    Pide datos por consola para el ingreso de un nuevo producto al catalogo

    :return: None
    """
    while True:
        codigo = input("Ingrese el codigo del producto: ")

        if not codigo.isdigit():
            print("El codigo debe ser un número")
            continue

        desc = input("Ingrese la descripción del producto: ")

        precio = input("Ingrese el precio del producto: ")
        precio = precio.split(".")
        if len(precio) != 2:
            print("El precio debe ser un número con dos decimales. Ej: 20.00")
            continue
        if len(precio[1]) != 2 or not precio[0].isdigit() or not precio[1].isdigit():
            print("El precio debe ser un número con dos decimales. Ej: 20.00")
            continue

        codigo = int(codigo)
        precio = float(".".join(precio))

        break

    try:
        productos.agregar(codigo, desc, precio)
    except Exception as e:
        print(e)
