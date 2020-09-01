def run(inicio, fin):
    """
    Imprimir en pantalla todos aquellos números que sean divisibles por 7 pero no sean divisibles por 5.

    :param inicio: int - inicio de la secuencia
    :param fin: int - fin de la secuencia
    :return: None
    """
    numeros = []
    for i in range(inicio, fin):
        if i % 7 == 0 and i % 5 != 0:
            print(i)
            numeros.append(i)
    print("\n" + ", ".join(map(str, numeros)))
