def runA(texto):
    """
    Ingresando un texto devuelve una lista con el texto dividio por comas

    :param texto: str - texto a dividir
    :return: list - lista con las palabras divididas
    """
    lista = texto.split(",")
    return lista


def runB(texto):
    """
    Ingresando un texto devuelve una lista con el texto dividio por comas y con los tipos de datos correspondientes

    :param texto: str - texto a dividir
    :return: list - lista con las palabras divididas
    """
    lista = texto.split(",")
    for i in range(len(lista)):
        # eval esta mal y es MUY inseguro! :)
        try:
            lista[i] = eval(lista[i])
        except SyntaxError:
            lista[i] = lista[i]
    return lista


def runC(lista):
    """
    Ingresando una lista de textos devuelve uns lista con el texto dividio por comas y con los tipos de datos correspondientes

    :param lista: list - lista de textos a dividir
    :return: list - lista con las palabras divididas
    """
    for i in range(len(lista)):
        lista[i] = runB(lista[i])
    return lista
