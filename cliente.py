import socket

print('Cliente connect4')

ipServidor="localhost"
puertoServidor=10000
nombre = socket.gethostname()
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((ipServidor, puertoServidor))
print("server: ",(ipServidor, puertoServidor))

while True:
    try:
        mensaje=input("--")
        cliente.send(mensaje.encode('utf-8'))
        respuesta = cliente.recv(1024)
        if mensaje=="salir":
            break
        print("->", respuesta.decode('utf-8'))
    finally:
        #cerrar conexion
        cliente.close()