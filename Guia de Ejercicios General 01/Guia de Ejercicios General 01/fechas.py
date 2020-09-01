import datetime


def crear_mes(nombre, abreviatura, cantidad):
    """
    Dados los parametros se imprime en consola un texto informativo
    :param nombre: str - nombre del mes
    :param abreviatura: str - abreviatura del mes
    :param cantidad: int - cantidad de dias del mes
    :return: None
    """
    devolucion = "Se creó el mes {mes}, que se abrevia {abreviacion} y contiene {dias} dias"
    print(devolucion.format(mes=nombre, abreviacion=abreviatura, dias=cantidad))


def imprimir_fecha_str(fecha):
    """
    Recibe como parametro un string con formato dd/mm/yyyy e imprime en consola
    la fecha dividida en dia, mes y año
    :param fecha: str - fecha en formato dd/mm/yyyy
    :return: None
    """
    try:
        fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y")
    except ValueError:
        raise Exception("Formato de fecha inválido!")
    print(f"El día ingresado fue: {fecha.day}")
    print(f"El mes ingresado fue: {fecha.month}")
    print(f"El año ingresado fue: {fecha.year}")
