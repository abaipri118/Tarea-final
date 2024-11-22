#Nombre: Adrian Baizan 
#Fecha: 10/10/24
#Objetivo: Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y escriba el mayor, el menor y la media aritmética

cantidad = int(input("¿Cuántos números va a introducir?"))


if cantidad < 0:
    print("¡Imposible!")
else:
    Lista = []
    for n in range(cantidad):
        numero = eval(input("Ingrese el número"))
        if numero >=0:
            Lista.append(numero)
    Suma = sum(Lista)
    Media = Suma/cantidad
    Mayor = max(Lista)#Me dice cual es el numero mayor de la lista en este caso
    Menor = min(Lista)#Me dice cual es el numero menor de la lista en este caso
    print("El numero mas pequeño de los introducidos es", Menor)
    print("El numero mas grande de los introducidos es", Mayor)
    print("La media de los numeros es", Media)