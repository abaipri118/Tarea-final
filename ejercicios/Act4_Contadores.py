#Nombre: Adrian Baizan 
#Fecha: 10/10/24
#Objetivo: Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

cantidad = int(input("¿Cuántos números va a introducir?"))

negativos = 0

if cantidad < 0:
    print("¡Imposible!")
elif cantidad ==0:
    print("No ha escrito ningun numero negativo")    
else:
    for n in range(cantidad):
            numero = float(input("Ingrese el número"))
            if numero < 0:
                negativos = negativos + 1
    print("Ha introducido", negativos, "números negativos.")