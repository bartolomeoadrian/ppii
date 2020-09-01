import fechas


def ejercicio_de_fechas():
    mes = input("Ingrese el nombre del mes: ")
    abreviatura = input("Ingrese la abreviatura: ")

    while True:
        dias = input("Ingrese la cantidad de dias: ")
        if dias.isdigit():
            dias = int(dias)
            break
        else:
            print("El valor ingresado es incorrecto, intentelo nuevamente!")

    fechas.crear_mes(mes, abreviatura, dias)


def ejercicio_de_fechas_con_formato():
    while True:
        try:
            fecha = input("Ingrese una fecha en formato dd/mm/yyyy: ")
            fechas.imprimir_fecha_str(fecha)
            break
        except Exception as e:
            print(e)


ejercicio_de_fechas_con_formato()
