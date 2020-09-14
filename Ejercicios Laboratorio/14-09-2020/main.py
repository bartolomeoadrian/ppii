from libs import reportes

envios = []

try:
    f = open(f"envios.txt", "r")
except Exception as e:
    print(e)
else:
    for linea in f.readlines():
        # Lo correcto seria utilizar un modelo para sanitizar todos estos datos, lo hago asi por un tema de tiempo
        linea = linea.split("-")

        envios.append({
            "id_envio": int(linea[0]),  # Habria que relevar si los 0 a la izquierda son relevantes para el sistema
            "descripcion": linea[1],
            "ciudad_origen": linea[2],
            "pais_origen": linea[3],
            "ciudad_destino": linea[4],
            "pais_destino": linea[5],
            "costo_envio": float(linea[6]),
            "peso": float(linea[7]),
            "pagado": True if str(linea[8]).strip() == "True" else False,
        })

    f.close()

reportes.generar_menos(envios)
reportes.generar_internacionales(envios)
reportes.generar_con_iva(envios)
reportes.generar_procesados(envios)
reportes.generar_posibles_perdidos(envios)
