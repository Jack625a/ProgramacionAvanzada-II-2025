#Estructura de un hilo

import threading, time

def bievenida(nombre):
    print(f"Hola bienvenido {nombre}")
    #Simular una tarea - tiempo de completar tarea 1s
    time.sleep(10)
    print(f"Completado...")

#Crear el hilo y ejecutar
hilo=threading.Thread(target=bievenida,args=("Kevin",))
hilo.start() #Inicializar el Hilo

#Esperar a que termine el proceso
hilo.join()
print("Hilo completado...")