#Varias tareas en simultaneo 
import threading, time

def tarea(a):
    time.sleep(1)
    print(f"Tarea {a} esta completada")

hilos=[]
for tareaEjecucion in range(5000):
    hiloEjecucion=threading.Thread(target=tarea, args=(tareaEjecucion,))
    hiloEjecucion.start()
    hilos.append(hiloEjecucion)

for hiloprocesado in hilos:
    hiloprocesado.join()
print("Todas las tareas completas...")