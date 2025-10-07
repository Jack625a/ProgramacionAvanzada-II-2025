import socket
import multiprocessing
import google.generativeai as genai

host="127.0.0.1"
puerto=5555

#Paso 1. Configurar la api
genai.configure(api_key="sus apis")

#Paso 2. Configurar el modelo
modelo=genai.GenerativeModel("gemini-2.0-flash-lite")

def manejarCliente(conexion,direccion):
    print(f"[+] Cliente conectado: {direccion}")
    try:
        while True:
            #Recibir el mensaje del cliente
            data=conexion.recv(1024).decode()
            if not data:
                break
            print(f"Cliente {direccion}: {data}")

            #Enviar el mensaje al Gemini
            respuesta=modelo.generate_content(data)
            mensaje=respuesta.text.strip()
            #Envio de la respuesta al usuario
            conexion.sendall(mensaje.encode())
    except Exception as e:
        print(f"Error con la conexion {direccion}: {e}")
    finally:
        conexion.close()
        print(f"[-] Cliente desconectado: {direccion}")

#Funcion principal
def principal(host,puerto):
    servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    servidor.bind((host,puerto))
    servidor.listen(5)
    print(f"Servidor activo {host}:{puerto}")

    while True:
        conexion,direccion=servidor.accept()
        proceso=multiprocessing.Process(target=manejarCliente, args=(conexion,direccion))
        proceso.start()


if __name__=="__main__":
    principal(host,puerto)

