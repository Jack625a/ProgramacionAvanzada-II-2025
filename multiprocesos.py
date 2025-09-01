#Importar el modulo de multiprocesos
import multiprocessing
import time


def tareas(n):
    print(f"Proceso {n} inicializado...")
    time.sleep(1)
    print(f"Proceso {n} completado...")

if __name__=="__main__":
    procesos=[]
    for iterador in range(1500):
        p=multiprocessing.Process(target=tareas,args=(iterador,))
        #INICIALIZAR EL PROCESO
        p.start()
        procesos.append(p)
    #Activar los procesos de forma paralela
    for p in procesos:
        p.join()

    print("Todos los procesos terminaron...")