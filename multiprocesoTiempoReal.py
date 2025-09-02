#ROLES DEL MULTIPROCESOS=> GIL
#VARIACION DE NUCLEOS REALES PARA PROCESAMIENTO

#MECANISMOS PARA MULTIPROCESOS
#1. PASAR DATOS ENTRE PROCESOS (QUEUE)
#2. CONEXION DIRECTA ENTRE DOS PROCESOS (PIPE)
#3. OBJETOS COMPARTIDOS (MANAGER)

#1. PASAR DATOS ENTRE PROCESOS (QUEUE)
from multiprocessing import Process,Queue
import time

#simulacion de una fabrica de chocolates
def produccion(chocolate):
    for iterador in range(1500):
        print(f"Produciendo el chocolate {iterador}")
        chocolate.put(iterador)
        time.sleep(0.2)

def distribucion(d):
    while True:
        dato=d.get()
        print(f"Distribuyendo el chocolate {dato}...")
        if dato==4:
            break

#Simulacion de lA PRODUCCION DE CHOCOLATE Y SU DISTRIBUCION CON 4 CAMIONES
if __name__=="__main__":
    distribuciondatos=Queue()
    #Proceso de produccion de chocolate
    p1=Process(target=produccion,args=(distribuciondatos,))
    #Proceso de distribucion del chocolate
    p2=Process(target=distribucion,args=(distribuciondatos,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

