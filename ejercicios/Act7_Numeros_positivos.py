#Nombre: Adrian Baizan 
#Fecha: 10/10/24
#Objetivo: Escriba un programa que pida la cantidad de números positivos que se tienen que
#escribir y a continuación pida números hasta que se haya escrito la cantidad de números
#positivos indicada.

cantidad = int(input("¿Cuántos números positivos desea introducir? "))


if cantidad <= 0:
    print("La cantidad debe ser mayor que 0")
else:
    positivos = []
    numeros_introducidos = 0

    while len(positivos) < cantidad: #len() devuelve el nuemero de elementos en la lista
        n = eval(input("Ingrese un número positivo"))
        numeros_introducidos = numeros_introducidos + 1
        if n > 0:
            positivos.append(n)  
    print("Ha introducido", numeros_introducidos, "numeros de los cuales", len(positivos), "positivos")
            

    

