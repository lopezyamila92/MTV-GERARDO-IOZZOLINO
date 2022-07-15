#set = {1,2,3,4,5,1,2}

#print(set)

#lista_1 = [1,2,3,4,5]
#lista_2 = list(set(lista_1))
#print(lista_2)

#print(list(set("pepe")))
              #FUNCIONES:::::
#ADD
#lista_1 = {"gera","yami","diego"}
#lista_1.add("rochi")
#print(lista_1)

#UPDATE
#lista_1 = {"gera","yami","diego"}
#lista_1.update(["rochi", "ana", "juan"])
#print(lista_1)
#len
#print(len(lista_1))
#discard
#lista_1 = {'yami', 'diego', 'gera', 'ana', 'rochi', 'juan'}
#lista_1.discard("ana")
#print(lista_1)

#remove
#lista_1 = {'yami', 'diego', 'gera', 'ana', 'rochi', 'juan'}
#lista_1.remove("ana")
#print(lista_1)
## in
#lista_1 = {'yami', 'diego', 'gera', 'ana', 'rochi', 'juan'}
#print("yami" in lista_1)

#grupo = {"mario", "andres", "ana", "ramon", "marta"}


#grupo_2 = {"marta", "andres"}

#grupo = grupo.difference(grupo_2)
#print(grupo)

#DICIONARIO
#mi_dic = {"provincia" :["cordoba", "san luis", "formosa"], "colores": ["amarillo", "azul", "rojo"], "age": 30, "name": "gera"}

#mi_dic["age"] += 1

#print(mi_dic)

######clase 7###
#upper/lower/capitalizar/tittle
#dato = "dieeeeeego sos sos sos crack"
#dato_1 = dato.upper()
#print(dato_1)

####count/find/rfind
#dato = "dieeeeeego sos sos sos crack"
#dato_1 = dato.count("sos")
#print(dato_1)

####count/find/rfind
#dato = "dieeeeeego sos sos sos crack"
#dato_1 = dato.find("chau")
#print (dato_1)
##split
#dato = "dieeeeeego          sos, alt sos, depor sos crack"
#dato_1 = dato.split(" ")
#print (dato_1)

### join
#dato = "diego sos alto sos crack"
#dato_1 = "y".join(dato)
#print(dato_1)


### remplace
#dato = "hola mundo mundo mundo mundo mundo"
#dato_1 = dato.replace("mu","",5)
#print(dato_1)


### insert

#lista = [1, 2, 3, 4, 5]
#lista.insert(2, 30)
#print(lista)

#sort
#lista = [4, 10, 3, 45, 5]
#lista.sort(reverse= True)
#print(lista)


#def ger_tiene_33():
#    print(f"el resultado es que tiene {30+3}")

#print("el perro es azul")

#ger_tiene_33()

#print("el perro es azul")

#ger_tiene_33()


#lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]



#lista.sort(reverse=True)
#print(lista)

#for impares in lista:
#    if (impares %2 == 1):
#        lista.remove(impares)
#print(lista)

#for numero in range(3,50,6):
#    print(f"el numero impar es {numero}")

#lista = [21,33,-25,85,-3.6, 27]    

#minimo = min(lista)

#print(minimo)

def calcular (op, a, b):
    if op == "sum":
        print(a+b)
    elif op == "res":
        print(a-b)

print(sum(50,100))
