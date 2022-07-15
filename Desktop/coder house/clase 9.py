#ejer 1
def area_rectangulo(a=(int(input("Ingrese base: "))), b=(int(input("Ingrese altura: ")))):
    area = (a * b)
    print(f"El area de su rectangulo es: {area}")

area_rectangulo()

import math

# ejer  2
def area_circulo(r):
    area = math.pi * (r * r)
    return print((f"El area de un circulo con radio {r} es {area}"))

area_circulo(5)

# ejer 3
def relacion(n1,n2):
    if n1 > n2:
        print("1")
    elif n1 < n2:
        print("-1")
    else:
        print("0")


relacion(5,10)
relacion(10,5) 
relacion(5,5)

# ejer 4
def intermedio(n1,n2):
    i = (n1 + n2) / 2
    print(f"El numero intermedio es {i}")

intermedio(-12,24)

#ejer 5

def recortar(recortar,limiteinferior,limitesuperior):
    if recortar < limiteinferior:
        return limiteinferior
    elif recortar > limitesuperior:
        return limitesuperior
    else:
        return {recortar}

print(recortar(15,0,10))

#ejer 6

def separar(lista):
    Lpares = []
    Limpares = []
    for i in lista:
        if i % 2 == 0:
            Lpares.append(i)
            Lpares.sort()
        else:
            Limpares.append(i)
            Limpares.sort()
    print(Lpares)
    print(Limpares)
    


separar([6,5,2,1,7])







