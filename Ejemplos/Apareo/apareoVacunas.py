FIN_ARCHIVO = ""
SIN_DEUDA = "$0"


def obtener_numero(cadena):
    lista = cadena.split("$")
    return int("".join(lista))


def actualizar_deuda(deuda, actualizacion):
    deuda = obtener_numero(deuda)
    actualizacion = obtener_numero(actualizacion)
    deuda_actualizada = deuda + actualizacion
    if deuda_actualizada == 0:
        return SIN_DEUDA
    return "+$" + str(deuda_actualizada) if deuda_actualizada > 0 else "-$" + str(abs(deuda_actualizada))


def leer_linea(archivo):
    linea = archivo.readline()
    return linea.rstrip("\n").split() if linea else (FIN_ARCHIVO, FIN_ARCHIVO)


def obtener_archivo(path):
    try:
        archivo = open(path)
    except FileNotFoundError:
        archivo = open(path, "w")
        archivo.close()
        archivo = open(path)

    return archivo


def agregar_nuevo_deudor(deudor, deuda, actualizaciones, nuevas_deudas):
    nuevo_deudor, deuda_extra = leer_linea(actualizaciones)
    while nuevo_deudor == deudor:
        deuda = actualizar_deuda(deuda, deuda_extra)
        nuevo_deudor, deuda_extra = leer_linea(actualizaciones)

    if not deuda == SIN_DEUDA:
        nuevas_deudas.write(deudor + " " + deuda + "\n")

    return nuevo_deudor, deuda_extra


def main():
    deudas = obtener_archivo("deudas.txt")
    actualizaciones = obtener_archivo("actualizaciones.txt")
    nuevas_deudas = open("nuevasDeudas.txt", "w")

    deudor_actual, deuda_actual = leer_linea(deudas)
    deudor_a_actualizar, deuda_actualizacion = leer_linea(actualizaciones)
    deuda_acumulada = deuda_actual

    while not deudor_actual == FIN_ARCHIVO and not deudor_a_actualizar == FIN_ARCHIVO:

        if deudor_actual == deudor_a_actualizar:
            deuda_acumulada = actualizar_deuda(deuda_acumulada, deuda_actualizacion)
            deudor_a_actualizar, deuda_actualizacion = leer_linea(actualizaciones)

        elif deudor_actual < deudor_a_actualizar:
            if deuda_acumulada != SIN_DEUDA:
                nuevas_deudas.write(deudor_actual + " " + deuda_acumulada + "\n")
            deudor_actual, deuda_actual = leer_linea(deudas)
            deuda_acumulada = deuda_actual

        else:
            deudor_a_actualizar, deuda_actualizacion = agregar_nuevo_deudor(deudor_a_actualizar, deuda_actualizacion, actualizaciones, nuevas_deudas)

    while not deudor_actual == FIN_ARCHIVO:
        nuevas_deudas.write(deudor_actual + " " + deuda_acumulada + "\n")
        deudor_actual, deuda_acumulada = leer_linea(deudas)

    while not deudor_a_actualizar == FIN_ARCHIVO:
        deudor_a_actualizar, deuda_actualizacion = agregar_nuevo_deudor(deudor_a_actualizar, deuda_actualizacion, actualizaciones, nuevas_deudas)

    deudas.close()
    actualizaciones.close()
    nuevas_deudas.close()

main()
