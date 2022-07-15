#Escribir una función que calcule el total de una factura tras aplicarle el IVA.
#La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
#Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def factura(valor, iva=1.21):
    return valor * iva    
print(factura(100))

#Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def media(lista):
    return sum(lista) / len(lista)
print(media([1,2,3,4,5]))

#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def cuadrados(lista):
    return (lista) 
print(cuadrados([10, 20, 30]))

