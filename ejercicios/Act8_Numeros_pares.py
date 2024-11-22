#Nombre: Adrian Baizan 
#Fecha: 10/10/24
#Objetivo: Escriba un programa que pida números pares mientras el usuario indique que quiere
#seguir introduciendo números. Para indicar que quiere seguir escribiendo números, el
#usuario deberá contestar S o s a la pregunta.

pares = 0
seguir = True

while seguir:
    n = int(input("Escriba un número par"))
    
    if n % 2 == 0:
        pares = pares + 1
    else:
        print("El número no es par, inténtelo de nuevo")

    continuar = input("¿Quiere escribir otro numero par? (S/N)")
    if continuar != "s":
        seguir = False


print("Ha escrito", pares, "numeros pares")
