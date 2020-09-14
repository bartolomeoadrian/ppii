from datetime import datetime
from random import randint


def abir_archivo_para_escribrir(ruta):
    """
    Devuelve un archivo para trabajar dada una ruta o lanza una excepcion en caso de no poder acceder al archivo.
    De no existir creará uno

    :param ruta: Str - Ruta del archivo
    :return: File
    """
    try:
        f = open(ruta, "w")
    except Exception as e:
        raise e
    else:
        return f


def generar_menos(envios):
    """
    Genera un nuevo archivo con nombre “menos.txt” donde se indique el identificador y la descripción
    de aquellos envíos cuyo identificador es menor o igual a 50000

    :param envios: Array - Array de envios en formato de diccionario
    :return: None
    """
    f = abir_archivo_para_escribrir("reportes/menos.txt")

    now = datetime.now()
    f.write(f"======================{now.strftime('%m/%d/%Y, %H:%M:%S')}======================\n")

    for envio in envios:
        if envio["id_envio"] < 50000:
            f.write(f"{envio['id_envio']}-{envio['descripcion']}\n")

    f.close()


def generar_internacionales(envios):
    """
    Genera un nuevo archivo con nombre “internacionales.txt” donde se muestren solamente toda la
    información de los envíos que son internacionales, es decir, donde el país origen difiera del
    país destino

    :param envios: Array - Array de envios en formato de diccionario
    :return: None
    """
    f = abir_archivo_para_escribrir("reportes/internacionales.txt")

    now = datetime.now()
    f.write(f"======================{now.strftime('%m/%d/%Y, %H:%M:%S')}======================\n")

    for envio in envios:
        if envio["pais_origen"] != envio["pais_destino"]:
            # Definitivamente quedaria mas prolijo usando un modelo
            f.write(f"{envio['id_envio']}-{envio['descripcion']}-{envio['ciudad_origen']}-{envio['pais_origen']}-{envio['ciudad_destino']}-{envio['pais_destino']}-{envio['costo_envio']}-{envio['peso']}-{envio['pagado']}\n")

    f.close()


def generar_con_iva(envios):
    """
    Genera un archivo “con_iva.txt” donde solamente contenga la descripción del envío, el peso y el
    costo aplicando la alícuota del IVA (21%)

    :param envios: Array - Array de envios en formato de diccionario
    :return: None
    """
    f = abir_archivo_para_escribrir("reportes/con_iva.txt")

    now = datetime.now()
    f.write(f"======================{now.strftime('%m/%d/%Y, %H:%M:%S')}======================\n")

    for envio in envios:
        f.write(f"{envio['descripcion']}-{envio['peso']}-{envio['costo_envio'] + ((21*envio['costo_envio']) / 100)}\n")

    f.close()


def generar_procesados(envios):
    """
    Genera otro archivo “procesados.txt” que contenga el identificador, la descripción en mayúscula, la
    fecha y hora actual y un numero aleatorio de 10 cifras, a modo de referencia. Además, en
    caso de no haber pagado el envío, también se debe agregar el precio

    :param envios: Array - Array de envios en formato de diccionario
    :return: None
    """
    f = abir_archivo_para_escribrir("reportes/procesados.txt")

    tiempo = datetime.now()
    f.write(f"======================{tiempo.strftime('%m/%d/%Y, %H:%M:%S')}======================\n")

    tiempo = tiempo.strftime('%m/%d/%Y, %H:%M:%S')

    for envio in envios:
        aleatorio = randint(1000000000, 9999999999)
        precio = envio["costo_envio"] if envio['pagado'] is False else ""
        f.write(f"{envio['id_envio']}-{str(envio['descripcion']).upper()}-{tiempo}-{aleatorio}-{precio}\n")

    f.close()


def generar_posibles_perdidos(envios):
    """
    Genera un archivo “posibles_perdidos.txt” donde se listen solamente los 10 productos
    que menores costos de envío tuvieron, ya que son probable que se pierdan en el camino.
    Para pensar: ¿se puede procesar en línea este pedido? ¿Es necesario algún almacenamiento
    temporal o no? ¿Serviría alguna estructura de datos en particular?

    :param envios: Array - Array de envios en formato de diccionario
    :return: None
    """
    f = abir_archivo_para_escribrir("reportes/posibles_perdidos.txt")

    now = datetime.now()
    f.write(f"======================{now.strftime('%m/%d/%Y, %H:%M:%S')}======================\n")

    f.close()
