#Nombre: Adrian Baizan 
#Fecha: 10/10/24
#Objetivo: Escriba un programa que pida dos números enteros y escriba la suma de todos los enteros desde el primer número hasta el segundo.


num1 = int(input("Ingrese el primer número entero"))
num2 = int(input("Introduce un numero mayor que el anterior"))

if num1<=0:
    print("Introduce un numero entero positivo")
elif num2==num1:
    print("Le he pedido un numero mayor que el anterior")
else: 
    num1<num2
    suma= sum(range(num1, num2 + 1))#sum() suma los valores dados
    print("La suma desde", num1,"hasta", num2, "es", suma)

