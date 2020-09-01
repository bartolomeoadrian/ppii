import math


def run(radio):
    """
    Devuelva una tupla conteniendo en el primer elemento el perímetro y en el segundo el área del mismo

    :param radio: int - radio del circulo
    :return: tupla - tupla conteniendo en el primer elemento el perímetro y en el segundo el área del mismo
    """
    return (2 * math.pi * radio), (math.pi * radio * radio)
