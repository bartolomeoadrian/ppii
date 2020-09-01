def run(texto):
    """
    Permite ingresar un texto cuyas palabras pondra en minuscula y retornara el conjunto sin palabras repetidas

    :texto: str - texto a trabajar
    :return: list - lista de palabras sin repetir
    """
    lista = texto.split(" ")
    for i in range(len(lista)):
        lista[i] = lista[i].strip().lower()
    return list(dict.fromkeys(lista))
