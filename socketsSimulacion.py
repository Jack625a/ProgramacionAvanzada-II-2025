#NIVEL BAJO PARA LA DISTRIBUCION DE PROCESOS
import socket

#PASO 1. CREAR EL SERVIDOR
servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#PASO 2. DEFINIR EL HOST Y EL PUERTO
servidor.bind(("localhost",5000))
#PASO 3. REALIZAR LA CONEXION DEL SERVIDOR
servidor.listen()
print("Iniciando Servidor...")

#PASO 4. ACEPTAR LA CONEXION PARA LA DISTRIBUCION
conexion,direccion=servidor.accept()
print(f"Servidor conectado al {direccion}")

#PASO 5. SIMULACION DEL SERVIDOR
data=conexion.recv(1024).decode()
print(f"Solicitud recibida... {direccion}")
conexion.sendall("Bienvenido...".encode())

#PASO 6. CERRAR LA CONEXION
conexion.close()
