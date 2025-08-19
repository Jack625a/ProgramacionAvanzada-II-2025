#Basicos de la sintaxis
#1. Variables - tipos de datos
nombre="Kevin"
numero=4.5
#1.2. Tipos de datos
#Tipos de datos Simples
#Numericos - Booleanos - Cadenas de Caracteres
color="Rojo"
edad=28
numero2=2.5
encender=True
#Tipos de datos Complejos
# Listas - Tuplas - Diccionarios
#Listas: Conjunto de datos ordenados o desordenados
#Son mutables - []
colores=["Rojo","Amarillo","Verde","Cafe"]
print(colores)
#Operaciones de las listas
#1. Insercion de datos (append)
colores.append("Celeste")
colores.append("Azul")
print(colores)
#Obtener un dato de la lista
print(colores[1])
print(colores[4])
colores.append("Lila")
#Para mostrar el ultimo dato de una lista [-1]
print(colores[-1])
#Actualizacion de datos
colores[0]="Anaranjado" 
print(colores)
#Eje. Modificar el color cafe de la lista de colores
#por el color Rosado

#Eliminacion de datos en una lista
#Eliminacion por el dato exacto
#remove("celeste")
colores.remove("Celeste")
print(colores)
#Eliminacion por id (pop(id))
colores.pop(-1)
print(colores)
#Vaciar la lista completa clear()
colores.clear()
print(colores)
#TUPLAS: Conjunto de datos ordenados o desordenados
#Son inmutables, (valor,valor,valor)
frutas=("Pera","Manzana","Naranja")
#Diccionarios: Conjunto estructurado de datos ordenados o desordenados
#Pares entre clave y valor {}
#Diccionario de estudiantes
estudiante={
    "nombre":"Kevin",
    "carrera":"Ingenieria de Sistemas",
    "edad":29,
    "correo":"k@gmail.com"
}
#Condicionales if else elif (==, !=, >=, <=)
num1=45
num2=15.8
if num1>=num2:
    print("El mayor es ",num1)
else:
    print("El mayor es ",num2)


#Multiples condiciones
#Menu de opciones
print("Menu")
print("1. Opcion1")
print("2. Opcion2")
print("3. Opcion3")
print("4. Opcion4")

opcion=input("Selecciones la opcion: ")
if opcion=="1":
    print("Opcion1")
elif opcion=="2":
    print("Opcion2")
elif opcion=="3":
    print("Opcion3")
elif opcion=="4":
    print("Opcion4")
else:
    print("Opcion Invalida")

#Bucles
#1. Bucles iterativos (repeticiones en un rango definido) for
#for iterador in range(inicio,stop,incremento):
for iterador in range(11):
    print(iterador)
#Eje1. mostrar los numero pares de 1 hasta el 100
for pares in range(0,101,2):
    print(pares)
#Eje1. mostrar los numero impares de 1 hasta el 100
for impares in range(1,100,2):
    print(impares)

#2. Bucles condicionados (repeticiones mientras se cumpla una condicion) while

a=1
while a<=10:
    print(a)
    a=a+1

#COMBINACION CON IF

while True:
    #Menu de opciones
    print("Menu")
    print("1. Opcion1")
    print("2. Opcion2")
    print("3. Opcion3")
    print("4. Opcion4")
    print("5. Salir")

    opcion=input("Selecciones la opcion: ")
    if opcion=="1":
        print("Opcion1")
    elif opcion=="2":
        print("Opcion2")
    elif opcion=="3":
        print("Opcion3")
    elif opcion=="4":
        print("Opcion4")
    elif opcion=="5":
        break
    else:
        print("Opcion Invalida")

#Eje1. Numero pares hasta 100
x=2
while x<=100:
    print(x)
    x=x+2

#Impares
x=1
while x<=100:
    print(x)
    x=x+2


#Funciones (conjunto ordenado de codigo reutilizable ) def
#SINTAXIS 
#def nombreFuncion(parametros):
#1. Funciones sin parametros
def bienvenida():
    print("Hola bienvenido")

#2. Funciones con paremtros
def sumar(a,b):
    return a+b

bienvenida()
print(sumar(8,11))

#Clases
#ATRIBUTOS - PROPIEDADES
#METODOS- ACCIONES (def)
#OBJETOS 
class Persona:
    def __init__(self,nombre,edad,ci):
        self.nombre=nombre
        self.edad=edad
        self.ci=ci
    #Metodos
    def dormir(self):
        print("Esta durmiendo...")
    def comer(self,comida):
        print("Esta comiendo ",comida)

persona1=Persona("Kevin",29,741111)
persona2=Persona("Ana",24,451221)
persona1.comer("Pan")
persona2.dormir()

#Importaciones
import numpy as np

