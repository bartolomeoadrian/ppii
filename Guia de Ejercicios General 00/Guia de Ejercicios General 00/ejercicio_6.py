def run():
    """
    Permite ingresar palabras que capitalizara y retornara el conjunto en orden alfabetico

    :return: list - lista de palabras ordenada alfabeticamente
    """
    lista = []
    print("Escriba 'exit' en cualquier momento para terminar la ejecucion")
    while True:
        print("Ingrese una palabra")
        palabra = input().capitalize()
        if palabra == "Exit":
            break
        lista.append(palabra)
    lista.sort()
    return lista
