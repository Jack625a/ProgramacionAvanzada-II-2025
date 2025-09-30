import socket
import threading
import time

import google.generativeai as genai

#Paso 1. Configurar el host y el puerto
host="127.0.0.1"
puerto=12345

#Paso 2. crear la lista de solicitudes
clientes=[]


#Paso 3. Funcion para manejar clientes
def manejar_Clientes(conexion,direccion):
    #PASO 2. CONFIGURAR LA API
    genai.configure(api_key="su api key")

    #PASO 3. CREAR EL MODELO
    modelo=genai.GenerativeModel("gemini-2.0-flash-lite")
   
    print(f"Nueva direccion: {direccion}")
    while True:
        try:
            mensaje=conexion.recv(1024).decode("utf-8")
            if not mensaje:
                break
            print(f"{direccion}: {mensaje}")
            respuesta=modelo.generate_content(contents=mensaje)
            respuestaTexto=respuesta.text
            print(respuestaTexto)
            conexion.sendall(respuestaTexto.encode("utf-8"))
            for cli in clientes:
                if cli !=conexion:
                    cli.sendall(mensaje.encode("utf-8"))
                    cli.sendall(f"{direccion}: {mensaje}".encode("utf-8"))
        except:
            break
    print(f"[-] Cliente Desconectado {direccion}")
    clientes.remove(conexion)
    conexion.close()

#Paso 4. Crear la funcion principal
def main():
    servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    servidor.bind((host,puerto))
    servidor.listen() #activo pára recibir solicitudes
    print(f"Servidor activo en el: {host}:{puerto}")

    while True:
        conexion,direccion=servidor.accept()
        clientes.append(conexion)
        hilo=threading.Thread(target=manejar_Clientes,args=(conexion,direccion))
        hilo.start()

if __name__=="__main__":
    main()
