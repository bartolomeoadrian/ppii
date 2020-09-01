def run():
    """
    Retorna un diccionario con claves de la A a la Z con sus valores en ASCII correspondientemente

    :return: dict - diccionario con claves de la A a la Z con sus valores en ASCII correspondientemente
    """
    diccionario = {}
    for i in range(97, 123):
        diccionario[chr(i)] = i
    return diccionario
