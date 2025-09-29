import socket
import threading

host="127.0.0.1"
puerto=12345

def recibir(sock):
    while True:
        try:
            mensajes=sock.recv(1024).decode("utf-8")
            if not mensajes:
                break
            print("\n[Mensaje]",mensajes)
        except:
            break

#Paso 3 Crear la funcion principal
def main():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((host,puerto))
    print("Conectado al chat Escribe tu mensaje: ")
    hilo=threading.Thread(target=recibir,args=(sock,))
    hilo.start()
    while True:
        mensaje=input("Ingrese su mensajes: ")
        #configurar comando para salir del bucle /salir
        if mensaje.lower()=="/salir":
            break
        sock.sendall(mensaje.encode("utf-8"))
    sock.close()

if __name__=="__main__":
    main()