import socket

#Paso1. Configurar el servidor
cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Paso2. Conexion al servidor (host, puerto)
cliente.connect(("localhost",5000))

#Paso 3. SIMULACION DE ENVIO DE DATOS
cliente.sendall("Hola Servidor...".encode())

#Paso 4. Obtner la respuesta
respuesta=cliente.recv(1024).decode()
print("Respuesta ",respuesta)


cliente.close()