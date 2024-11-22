#Nombre: Adrian Baizan 
#Fecha: 10/10/24
#Objetivo: Mejore la usabilidad del programa anterior haciendo que la pregunta se repita si el
#usuario no contesta S, s, N o n.

pares = 0
seguir = True

while seguir:
    n = int(input("Escriba un número par"))
    
    if n % 2 == 0:
        pares = pares + 1
    else:
        print("El número no es par, inténtelo de nuevo.")

    while True:
        continuar = input("¿Quiere escribir otro número par? (S/N)")
        if continuar in ['s', 'n']: #in se utiliza para comprobar si un elemento esta en una lista, tupla o conjunto
            break  # break es para salir del bucle
        else:
            print("Respuesta no válida. Ingrese s/n")

    if continuar == 'n':
        seguir = False 

print("Ha escrito", pares, "números pares.")
