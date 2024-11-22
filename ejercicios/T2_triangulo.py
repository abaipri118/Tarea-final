#Nombre: Adrian Baizan
#Fecha: 14/10/24 
# Objetivo: Escriba un programa que pida la anchura y altura de un rectángulo y lo dibuje con
#caracteres producto (*):


# Solicitar la anchura del triángulo
anchura = int(input("Introduce la anchura del triángulo: "))

# Dibujar el triángulo
for n in range(1, anchura + 1):
    print('*' * n)

for n in range(anchura -1, 0, -1):
    print('*' * n)