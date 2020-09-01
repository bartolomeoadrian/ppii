def run(numero):
    """
    Factorea un numero de manera iterativa

    :param numero: int - numero a factorear
    :return: int - numero factoreado
    """
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial


def recursivo(numero):
    """
    Factorea un numero de manera recursiva

    :param numero: int - numero a factorear
    :return: int - numero factoreado
    """
    if numero <= 0:
        return 1
    return numero * recursivo(numero - 1)
