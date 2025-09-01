#IMPORTAR LOS MODULOS 
from multiprocessing import Pool
import time

#Accion a ejecutar
def ejecucion(n):
    print(f"Iniciando {n} tarea...")
    time.sleep(1)
    return n*n

if __name__=="__main__":
    with Pool(processes=8) as pool:
        numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        resultados=pool.map(ejecucion,numeros)
    print(resultados)