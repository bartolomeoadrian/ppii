try:
    f = open("texto.txt", "r")
except Exception as e:
    print(e)
else:
    # Es recomendable leer asi un archivo? O es mejor linea por linea?
    texto = f.read()
    mayus, minus, espec = 0, 0, 0

    for i in texto:
        if i.isalpha():
            if i.isupper():
                mayus += 1
            else:
                minus += 1
        else:
            espec += 1

    f.close()

    print(f"La cantidad de mayúsculas es: {mayus}")
    print(f"La cantidad de minúsculas es: {minus}")
    print(f"La cantidad de otros caracteres es: {espec}")
