# Modo de uso:
#
# Use: ./OUILookup --ip <IP> | --mac <IP> [--help]
#
#	--ip : specify the IP of the host to query.
#	--mac: specify the MAC address to query. P.e. aa:bb:cc:00:00:00.
#	--help: show this message and quit.

import getopt
import sys
    
#Cuerpo principal
def main():
    try:
        options, args = getopt.getopt(sys.argv[1:],"i,m",['ip=','mac=','help'])
    except:
        print("Error: Parametros incorrectos.")
        uso()
        
    IP = None
    MAC  = None
    
    for opt, arg in options:
        if opt in ('--help'):
            uso()
        if opt in ('--ip'):
            IP = str(arg)
        elif opt in ('--mac'):
            MAC = str(arg)
            
    #IP o MAC deben ser ingresadas.
    if IP == None and MAC == None:
        uso()
    elif IP != None and MAC == None:
        #buscar_IP()
        print("Vacio")
    elif IP == None and MAC != None:
        buscar_MAC(MAC)

# ----- #

def uso():
    print("Uso: ./" + sys.argv[0] + " --ip <IP> | --mac <MAC> [--help] ")
    print("\nParametros:")
    print("     --ip: Especifique el IP del host para consultar")
    print("     --mac: Especifique la dirección MAC a consultar. P.e. aa:bb:cc:00:00:00.")
    print("     --help: Muestra esta pantalla y termina.")
    exit(1)
    
    
#
# Buscar
# Entrada: 
#          MAC: Direccion MAC a consultar.
# Salida:
#          MAC: Direccion MAC que se consulta.
#          Vendor: Fabricante de la tarjeta de red.
#

def buscar_MAC(MAC):
    archivo = "vendor.txt"
    linea_mac= MAC.split(":") # Separa la MAC para poder ser buscada
    n_mac = (linea_mac[0] + ":" + linea_mac[1] + ":" + linea_mac[2]) # Toma las 3 primeras partes de la direccion MAC
    busqueda = n_mac.upper() # Palabra a buscar

    with open(archivo, "r") as archivo_lectura: #Dado el archivo, lo abre y comienza la busqueda por linea.
        for linea in archivo_lectura:
            linea = linea.rstrip()
            vendor = linea.split("\t") # Separa las lineas por "\t"
            if busqueda in vendor: # Si la MAC que se esta buscando se encuentra en la linea muestra lo siguiente
                print("MAC address  : ", MAC)
                print("Vendor       : ", vendor[2])
            else:
                print("MAC address  : ", MAC)
                print("Vendor       :  Not found")
                break

#Esto se utiliza para poder importar este codigo en otro script para utilizar sus funciones.
if __name__ == '__main__':
    main()