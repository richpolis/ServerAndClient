#!/usr/bin/env python
# -*- coding: utf-8 -*-

# importamos el modulo socket
import socket
import logging
import logging.handlers
from imei import Imei
from insert_imei import insert_imei

# instanciamos un objeto para trabajar con el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Con el metodo bind le indicamos que puerto debe escuchar y de que servidor esperar conexiones
# Es mejor dejarlo en blanco para recibir conexiones externas si es nuestro caso
s.bind(("", 9991))

# Aceptamos conexiones entrantes con el metodo listen, y ademas aplicamos como parametro
# El numero de conexiones entrantes que vamos a aceptar
s.listen(1)

# Instanciamos un objeto sc (socket cliente) para recibir datos, al recibir datos este
# devolvera tambien un objeto que representa una tupla con los datos de conexion: IP y puerto
sc, addr = s.accept()

# Creamos una instancia al logger con el nombre especificado
logger = logging.getLogger('imei')

# Indicamos el nivel máximo de seguridad para los mensajes que queremos que se
# guarden en el archivo de logs
# Los niveles son:
#   DEBUG - El nivel mas alto
#   INFO
#   WARNING
#   ERROR
#   CRITIAL - El nivel mas bajo
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='log.log', level=logging.DEBUG)

# Creamos una instancia de logging.handlers, en la cual vamos a definir el nombre
# de los archivos, la rotación que va a tener, y el formato del mismo

# when - determina cada cuando se rota el archivo:
#   'S' Seconds
#   'M' Minutes
#   'H' Hours
#   'D' Days
#   'W' Week day (0=Monday)
#   'midnight'  Roll over at midnight
# interval - determina el intervalo, por ejemplo si indicamos minutos, interval
# equivale al numero de minutos.
# Si backupCount=0, no eliminara ningún fichero rotado
handler = logging.handlers.TimedRotatingFileHandler(filename='log.log',  when="H", interval=1, backupCount=0)

# Definimos el formato del contenido del archivo de logs
formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%y-%m-%d %H:%M:%S')
# Añadimos el formato al manejador
handler.setFormatter(formatter)

# Añadimos el manejador a nuestro logging
logger.addHandler(handler)

while True:

    print "Servidor escuchando proxima instruccion"

    # Recibimos el mensaje, con el metodo recv recibimos datos y como parametro
    # la cantidad de bytes para recibir
    recibido = sc.recv(1024)

    # Si el mensaje recibido es la palabra close se cierra la aplicacion
    if recibido == "close":
        break

    # Si se reciben datos nos muestra la IP y el mensaje recibido
    print str(addr[0]) + " Recibido: ", recibido

    logging.debug("Recibido: %s" % (recibido,))

    # guardando los datos
    imei = Imei()
    imei.set_data(recibido)
    sql = imei.get_query_insert()
    args = imei.get_args_insert()

    response = insert_imei(sql, args)
    logging.debug("Respuesta: %s" % (response,))
    # Devolvemos el mensaje al cliente
    sc.send(recibido)

print "Adios."

# Cerramos la instancia del socket cliente y servidor
sc.close()
s.close()
