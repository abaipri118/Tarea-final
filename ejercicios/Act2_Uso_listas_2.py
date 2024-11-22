#Nombre: Adrian Baizan 
#Fecha: 10/10/24
#Objetivo: Un programa que pida dos numeros y de una lista de sus numeros consecutivos

n1 = int(input("Escribe un numero entero"))
n2 = int(input("Escribe otro numero entero"))

if n1<n2:
    print(list(range(n1, n2+1)))
else:
    n2>n1
    print(list(range(n2+1, n1)))

