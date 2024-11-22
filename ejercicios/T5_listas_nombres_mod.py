#Nombre: Adrian Baizan
#Fecha: 14/10/24 
# Objetivo: Escriba un programa que pida cuántas listas se quieren crear y las solicite a
#continuación 

Numero_lista = int(input("Introduce el numero de lista a introducir"))

Lista = []


for n in range(0,Numero_lista):
    Lista1 = []
    palabras = int(input("Numero de palabras a introducir lista "))

    for i in range(0,palabras):
        Intro = input("Digame la palabra")
        Lista1.append(Intro)
    Lista.append(Lista1)

print("Listas creadas:")
print(Lista)

