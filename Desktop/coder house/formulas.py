variable = 32
print(f"gera tiene:{variable}")
# prueba de f

edad = 31
peso = 50
altura = 1.50
print(f"EDAD:{edad}años peso{peso}kg altura{altura}metros")
# variable combinadas

nombre = "gerardo"
print(f"mi nombre es {nombre}")

#funciones de listas
# append
numeros = [1,2,3,4]
numeros.append(5)
print(numeros)

#len
numeros = [1,2,3,4,5]
print(len(numeros))

# pop
numeros = [1,2,3,4]
numeros.pop()
print(numeros)

#ejercicios
lista1 = [1, 12, 123]
lista1.append(1234)
lista1.append("hola")
print(lista1)

#lista 2
lista2 = ['bye', 'ciao', 'agur', 'adieu']
lista2.append("adios")
lista2.append(1234)
print(lista2)

#lista
lista3 = [1, 12, 123]
lista3.pop()
print(lista3)

#lista4
lista4 = ['bye', 'ciao', 'agur', 'adieu']
lista4[:1] = []
lista4.pop()
print(lista4)

#lista 5
print(lista4+lista3)

# lista 6
lista55 = ['bye', 'ciao', 'agur', 'adieu']
lista55.insert(2, "gato")
print(lista55)