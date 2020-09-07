def fibonacci_recursiva(numero):
    """
    Calcula la serie fibonacci de manera recursiva

    :param numero: int - Posicion de la serie a calcular
    :return: int - Valor de la serie en esa posicion
    """
    if numero == 0:
        return 0
    if numero == 1:
        return 1
    return fibonacci_recursiva(numero - 1) + fibonacci_recursiva(numero - 2)


def fibonacci_iterativo(numero):
    """
    Calcula la serie fibonacci de manera iterativa

    :param numero: int - Posicion de la serie a calcular
    :return: int - Valor de la serie en esa posicion
    """
    fibo, pri, seg = None, 0, 1
    for i in range(1, numero):
        fibo = pri + seg
        pri = seg
        seg = fibo
    return fibo


def plazo_fijo(inicial, interes, meses):
    """
    Calcula los intereses de un plaza fijo dados los interes

    :param inicial: int - Monto inicial
    :param interes: int - Interes del plazo fijo
    :param meses: int - Meses al calcular el plazo fijo
    :return: int - Monto final
    """
    if meses == 0:
        return 0
    else:
        mes_siguiente = plazo_fijo(1, interes, meses - 1) or 1
        return inicial * (1 + interes) * mes_siguiente


fib_rec = fibonacci_recursiva(5)
print(fib_rec)

fib_ite = fibonacci_iterativo(5)
print(fib_ite)

p_fijo = plazo_fijo(10, 1, 2)
print(p_fijo)
