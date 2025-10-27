#Paso 1. IMPORTACIO DE DEPENDENCIAS
import socket
import multiprocessing
import google.generativeai as genai

#Paso 2. DEFINIR EL HOST Y EL PUERTO
host="127.0.0.1"
puerto=1234

#Paso 3. Configurar la Api
genai.configure(api_key="")

#Paso 4. Configurar el modelo
modelo=genai.GenerativeModel("gemini-2.0-flash-lite")

#Paso 5. Crear la funcion para conectar al modelo
def procesar(colaPeticiones,colaRespuestas):
    while True:
        try:
            clienteId, mensaje=colaPeticiones.get()
            if mensaje=="__salir__":
                break
            print(f"[SERVIDOR] Procesando mensajes {clienteId}: {mensaje}")
            respuesta=modelo.generate_content(mensaje)
            texto=respuesta.text.strip()
            if respuesta and respuesta.text:
                return respuesta 
            else: "No se obtuvo el mensaje"
            colaRespuestas.put((clienteId,texto))
        except Exception as e:
            print(f"Error al obtener el mensaje {e}")

#Funcion para manejar cada cliente
def manejarCliente(conexion,direccion,clienteId,colaPeticiones,colaRespuestas):
    print(f"[Servidor]- Cliente conectado: {direccion}")
    try:
        while True:
            data=conexion.recv(1024).decode("utf-8")
            if not data:
                break
            if data.lower()=="salir":
                print(f"[Servidor] - Cliente desconectado {direccion}")
                break
            print(f"[Servidor] Mensaje recibido de {direccion}: {data}")
            colaPeticiones.put((clienteId,data))
            #Esperar la respuesta modelo
            while True:
                clienteRespuesta,texto=colaRespuestas.get()
                if clienteRespuesta==clienteId:
                    conexion.sendall(texto.encode("utf-8"))
                    break
    except Exception as e:
        print(f"[Servidor] Error con el procesamiento del cliente {direccion}: {e}")

    finally:
        conexion.close()

#funcion principal del servidor
def servidor():
    colaPeticiones=multiprocessing.Queue()
    colaRespuestas=multiprocessing.Queue()

    #Crear el modelo para el manejo de solicitudes
    procesoModelo=multiprocessing.Process(target=procesar, args=(colaPeticiones,colaRespuestas))
    procesoModelo.start()

    #Configurar el servidor
    servidorSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    servidorSocket.bind((host,puerto))
    servidorSocket.listen(5)
    print(f"[Servidor] - Servidor Activo en {host}:{puerto}")
    clienteId=0
    try:
        while True:
            conexion, direccion=servidorSocket.accept()
            clienteId+=1
            procesoCliente=multiprocessing.Process(target=manejarCliente,args=(conexion,direccion,clienteId,colaPeticiones,colaRespuestas))
            procesoCliente.start()
    except KeyboardInterrupt:
        print(f"[Servidor] Cerrando servidor...")
    finally:
        colaPeticiones.put((None,"__salir__"))
        procesoModelo.join()
        servidorSocket.close()

if __name__=="__main__":
    servidor()