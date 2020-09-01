def run(texto):
    """
    Recibo por parámetro un texto, y que devuelva una tupla conteniendo en el
    primer lugar, la cantidad de letras (mayúsculas o minúsculas), en el segundo lugar la cantidad de dígitos
    numéricos y en el tercer lugar, otros símbolos.

    :param texto: str - texto a trabajar
    :return: tuple - tupla con las cantidades correspondientes
    """
    return sum(i.isalpha() for i in texto), sum(i.isdigit() for i in texto), sum((not i.isalpha() and not i.isdigit()) for i in texto)
