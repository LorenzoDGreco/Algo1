def leer_info(archivo):
    linea = archivo.readline()
    if linea:
        registro = linea.rstrip("\n").split(",")
    else:
        registro = ['999999','0']
    return registro

def main():
    cajero = open("cajero.csv", "r")
    online = open("online.csv", "r")
    sucursal = open("sucursal.csv", "r")

    max = "999999"
    cajero_cta, cajero_importe = leer_info(cajero)
    online_cta, online_importe = leer_info(online)
    sucursal_cta, sucursal_importe = leer_info(sucursal)

    total = 0

    while cajero_cta != max or online_cta != max or sucursal_cta != max:
        tot_cuenta = 0
        menor = min(cajero_cta, online_cta, sucursal_cta)
        print("cuenta: ", menor)
        while cajero_cta == menor and cajero_cta != max:
            tot_cuenta += int(cajero_importe)
            cajero_cta, cajero_importe = leer_info(cajero)
        while online_cta == menor and online_cta != max:
            tot_cuenta += int(online_importe)
            online_cta, online_importe = leer_info(online)
        while sucursal_cta == menor and sucursal_cta != max:
            tot_cuenta += int(sucursal_importe)
            sucursal_cta, sucursal_importe = leer_info(sucursal)
        print("Total por Cuenta: ", tot_cuenta)
        total += tot_cuenta
    print("Total General: ", total)
    cajero.close()
    online.close()
    sucursal.close()

main()