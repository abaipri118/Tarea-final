#Nombre: Adrian Baizan 
#Fecha: 10/10/24
#Objetivo: Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores

numero = int(input("Escriba un numero mayor de cero"))

if numero<=0:
    print("¡Escriba un numero mayor que cero!")
else:
    Divisores = []
    for n in range(1, numero + 1):
        if numero % n == 0:
            Divisores.append(n)#.append añade los valores a la lista
            
        
    print("Los divisores de", numero, "son:", Divisores)
