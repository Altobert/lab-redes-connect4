import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)


def menu():
    while True:
        eleccion = input("1- Jugador vs Máquina"
                         "\n"
                         "2- Salir"
                         "\n"
                         "Elige: ")
        if eleccion == "1":
            "Por defecto 6 filas 6 columnas"
            filas, columnas = 6, 6
            while True:
                tablero = crear_tablero(filas, columnas)
                jugador_vs_computadora(tablero)
                if not volver_a_jugar():
                    break
        
        if eleccion == "2":
            break


while True:
    # Wait for a connection
    print('waiting for a connection')
    menu()
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True: 
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()