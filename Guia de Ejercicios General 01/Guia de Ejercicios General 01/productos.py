catalogo = [
    {'codigo': 1221, 'desc': "Leche entera 1 litro", 'precio': 54.34},
    {'codigo': 2231, 'desc': "Queso untable 200gs", 'precio': 145.34},
    {'codigo': 3213, 'desc': "Harina 0000 1 kilo", 'precio': 24.32},
    {'codigo': 3431, 'desc': "Detergente Biodeg.", 'precio': 80.14},
    {'codigo': 5431, 'desc': "Jabon cremoso 1 unidad", 'precio': 50.00},
    {'codigo': 1233, 'desc': "Arroz Integral 1 kilo", 'precio': 66.33},
    {'codigo': 1589, 'desc': "Gaseosa Cola 1 Litro", 'precio': 78.65},
    {'codigo': 985, 'desc': "Cerveza Rubia lata 476", 'precio': 54.00},
    {'codigo': 84, 'desc': "Manteca Pack 500gs", 'precio': 124.65},
    {'codigo': 155, 'desc': "Fideos Tallarin 1 kilo", 'precio': 35.23},
    {'codigo': 9857, 'desc': "Jamon Cocido 200 gs", 'precio': 99.32},
    {'codigo': 4756, 'desc': "Queso Dambo 200 gs", 'precio': 98.34},
    {'codigo': 5661, 'desc': "Patitas de Pollo 400 gs", 'precio': 144.99},
    {'codigo': 1763, 'desc': "Comida Gatos 500gs", 'precio': 86.25},
    {'codigo': 1356, 'desc': "Tostaditas Light 265 gs", 'precio': 32.50},
    {'codigo': 1524, 'desc': "Salchichas Super Pancho", 'precio': 95.20},
    {'codigo': 7341, 'desc': "Salsa de Tomate 500 gs", 'precio': 47.90}
]


def buscar(codigo):
    """
    Busca un producto en el catalogo a traves de su codigo

    :param codigo: int - codigo del producto a buscar
    :return: None or dict - devuelve None si no se encontro el producto o un diccionario si lo encontro
    """
    for producto in catalogo:
        if producto["codigo"] == codigo:
            return producto
    return None


def agregar(codigo, desc, precio):
    """
    Agrega un nuevo producto al catalogo

    :param codigo: int - codigo del producto
    :param desc: str - descripcion del producto
    :param precio: float - precio del producto
    :return: None
    """
    producto = buscar(codigo)
    if producto:
        raise Exception("Ya existe un producto con ese código!")

    if not type(codigo) is int:
        raise Exception("El código debe ser un entero!")

    if not type(desc) is str:
        raise Exception("La descripcion debe ser un string!")

    if not type(precio) is float:
        raise Exception("El precio debe ser un float!")

    catalogo.append({
        'codigo': codigo,
        'desc': desc,
        'precio': precio
    })
