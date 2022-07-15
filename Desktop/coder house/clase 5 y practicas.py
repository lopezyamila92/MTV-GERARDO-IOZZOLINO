# ejercicio

#nombre = input("ingrese su nombre:")
#edad = int(input("ingrese su edad:"))

#validacion1 = nombre != "****"
#validacion2 = 10 < edad < 18
#validacion3 = 3 <= len(nombre) < 18
#validacion4 = (edad*4) > 40
 
#respuesta = validacion1 and validacion2 and validacion3 and validacion4

#print(respuesta)

#nombre = input("ingrese su nombre:")
#edad = int(input("ingrese su edad:"))

#edad = edad + 1

#print(edad)

#edad = int(input("ingrese su edad:"))

#if (edad) < 18 :
#    print("eres guapo")
#elif (edad) < 30 :
#    print("tenes los huevos semi inf")
#elif (edad) < 45 :
#    print("tenes los huevos medio inflado")
#elif (edad) < 60 :
#    print("huevos duros mal")
#else:
#    print("crack")

#print("fin de ejecucion")


#Nombre = input("ingrese su Nombre :")
#preferencia = input("ingrese su preferencia M o C :")
#if Nombre[0] < "m":
#    if preferencia == "M":
#        print("eres grupo a con marvel")
#elif Nombre[0] > "m" and preferencia == "C" :
#        print("eres grupo a con CAPCOM")
#else:
#    print("eres grupo B")

#n = int(input("ingrese el numero:"))
#i = 0

#while(i < n):
#    print("imprimimos el valor de i")
#    print(i)
#    i = i + 1

#contrasena = "Gerar12"

#valor_ingresado = input("ingrese la contraseña:")

#while (valor_ingresado != contrasena):
#    valor_ingresado = input("te equivocaste, vovlve a intentar:")

#print("bienvenido")

#valor = int(input("ingrese valores :"))
#while (valor != 0):
#    valor_ingresado = input("te equivocaste, vovlve a intentar:")
#else:
#    print(correcto)

#n = int(input("ingrese el numero:"))
#i = 1
#while (i < n):
#    print("valor de i")
#    print(i)
#    i += 1

#n = 0
#while n < 5:
#    n += 1
#    print("n vale", n)
#ejercico 5
#lista = [1, 3, 6, 9]
#variable = int(input("ingrese el numero:"))
#while (variable > 0 and variable > 9):
#    print("no ingres numero entre 0 y 9")
#    variable = int(input("ingrese el numero entre 0 y 9:")) 
#if variable in lista:
#    print("esta en la lista")
#else:
#    print("no esta")
#ejercicio 7
#lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
#lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
#lista_nueva = []
#for diego in lista_1:
#    if diego not in lista_nueva:
#        lista_nueva.append(diego)
#for diego in lista_2:
#    if diego not in lista_nueva:
#        lista_nueva.append(diego)
#print(lista_nueva)

#n = int(input("ingrese un numero"))
#i = 1

#while (i < n):
#    print("valor de i")
#    print(i)
#    i += 1

#contrasena = "yamila12"
#valor_ingresado = input("ingrese un contrasena:")
#while (valor_ingresado != contrasena):
#    valor_ingresado = input("error,ingrese un contrasena:")

#print("ingreso")

#n = int(input("ingrese un numero"))
#i = 1

#while (i < n):
#    if(i > 10):
#        break
#    print(i)
#    i += 1

#n = int(input("ingrese un numero"))
#i = 1


#while (i < n):
#    if(i > 10):
#        break
#    print(i)
#    i += 1
#else:
#    print("imprimio numeros")



#n = int(input("ingrese un numero: "))
#acumulador=0
#while(n != 0):
#    acumulador = acumulador +  n
#    n = int(input("ingrese otro numero, 0 para terminar:"))
#
#print(acumulador)

#lista = [10,20,20]
#lista2 = []

#for num in lista:
#    lista2.append(num*2)

#print(lista2)

#edad = 28 
#if (edad >= 18):
#    print("sos mayor")
#else:
#    print("la persona es menor")


#calificacion = int(input("ingrese su calificacion"))

#if (calificacion == 10):
#   print("perfecto")
#elif (9 >= calificacion >= 8):
#    print("felicitaciones")
#elif (7 >= calificacion >= 6):
#    print("felicitaciones")
#else:
#    print("reprobado")


#valor = 100

#while (valor < 9):
#    print("gera")
#    valor = valor + 1
#else:
#    print("el valor inicial de la variable ")

#nombre = ""

#while nombre != "tomas":
#    nombre = input ("ingrese el nombre:")

#numero = 99

#suma_numero = 0

#while numero != 0:
#    numero = int(input("ingrse el numero:"))
#    suma_numero = suma_numero + numero
#print("la suma total de los numero es :" , suma_numero )


#nombre_apellido = "damian sousa"

#for letra in nombre_apellido:
#    print(letra)

#usuarios = ["gera", "yami", "laura", "pao"]
#print(usuarios[0])
#for fff in usuarios:
#    print(fff)

### range

#for i in range(10):
#    print("indice de range", i)

## enumerat 
#usuarios = ["gera", "yami", "laura", "pao"]
#for indice, usuario in enumerate(usuarios):
#    print(indice, usuario)





#edad = int(input("ingrese un valor:"))
#while (edad < 18):
#    print("eres chico")
#    if (edad > 18)
#    int(input("ingrese un valor:"))
#else:
#    print("puedes entrar")

# Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:


# 1--Mostrar una suma de los dos números
# 2--Mostrar una resta de los dos números (el primero menos el segundo)
# 3--Mostrar una multiplicación de los dos números
# 4--Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
# 5--En caso de no introducir una opción válida, el programa informará de que no es correcta.

#ejercicio 1

#valor_1 = int(input("ingrese un valor:"))
#valor_2 = int(input("ingrese un valor:"))

#menu = int(input("ingrese un valor 1-2-3-4:"))

#if (menu == 1):
#    print(valor_1 + valor_2)
#elif (menu == 2):
#        print(valor_1 - valor_2)
#elif (menu == 3):
#        print(valor_1 * valor_2) 
#elif (menu == 4):
#        print("fin del programa")
#else:
#    print("no es correcto")  

#Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar,
# debe repetirse el proceso hasta que lo introduzca correctamente.

#valor = int(input("ingrese un valor:"))

#while numero != 0:
#    numero = int(input("ingrse el numero:"))
#    suma_numero = suma_numero + numero
#print("la suma total de los numero es :" , suma_numero )



#nombres = ["ana", "elisa", "pablo", "tamara", "zamudio"]

#nuevo_nombre = "jorge"

#for index, nombre in enumerate(nombres):
#    if nuevo_nombre < nombre:
#        nombres.insert(index, nuevo_nombre)
#        break

#print(nombres)

#set_1 = set(range(10))
#print(set_1)

#auto = 1 
#while auto <= 50:
#    print(auto)
#    auto = 1

#print ("fin de programa")



#ingrese = input("desea ingresar al programa?:")
#while (ingrese == "si"):
#        ingrese=(input("desea ingresar al programa?:"))
#else:
#    print("se termino")
        
#Escriba_su_contrasena_1 = input("ingrese contasena_1:")
#Escriba_su_contrasena_2 = input("ingrese contasena_2:")
#acumulador = 1
#while acumulador < 3:
#    if Escriba_su_contrasena_1 != Escriba_su_contrasena_2:
#        Escriba_su_contrasena_1 = input("ingrese contasena_1:")
#        Escriba_su_contrasena_2 = input("ingrese contasena_2:")
#        acumulador += 1
#    elif Escriba_su_contrasena_1 == Escriba_su_contrasena_2:
#        print("ingreso al sistema")
#        break            
#else:
#        print("bloqueado")


#ejercicio 1

#valor_1 = int(input("ingrese un valor:"))
#valor_2 = int(input("ingrese un valor:"))

#menu = int(input("ingrese un valor 1-2-3-4:"))

#if (menu == 1):
#    print(valor_1 + valor_2)
#elif (menu == 2):
#        print(valor_1 - valor_2)
#elif (menu == 3):
#        print(valor_1 * valor_2) 
#elif (menu == 4):
#        print("fin del programa")
#else:
#    print("no es correcto") 

#ejercicio 2

#numero = int(input("ingrese el numero:"))

#while (numero%2 != 1):
#    int(input("ingrese el numero:"))    
#print(f"su numero impar es {numero}")

#ejercicio 3

#print(sum(list(range(1,100,2))))

#ejercicio 4

#cantn = int(input("cantidad de numero a ingresar:"))

#acumulador = 0
#cantidad_vueltas = 0
#while cantidad_vueltas < cantn:
#    n1 = int(input("ingrese  numero :"))
#    acumulador = acumulador + n1
#    cantidad_vueltas += 1

#print(acumulador / cantn)




#ejercico 5
#lista = [1, 3, 6, 9]
#variable = int(input("ingrese el numero:"))
#while (variable >= 0 and variable >= 9):
#    print("no ingres numero entre 0 y 9")
#    variable = int(input("ingrese el numero entre 0 y 9:")) 
#if variable in lista:
#    print("esta en la lista")
#else:
#    print("no esta")

#ejercico 6

#print(list(range(0,11,1)))
#print(list(range(-10,1,1)))
#print(list(range(0,21,2)))
#print(list(range(-19,0,2)))
#print(list(range(0,51,5)))


#ejercicio 7
#lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
#lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
#lista_3 = []

#for primera_busqueda in lista_1:
#    for segunda_busqueda in lista_2:
#        if (primera_busqueda == segunda_busqueda) and (primera_busqueda not in lista_3):
#            lista_3.append(primera_busqueda)
#print(lista_3)
#ciudades = [
#    {"id":1,"city":"Buenos Aires","country":"Argentina"},
#    {"id":2,"city":"Puerto Quijarro","country":"Bolivia"},
#    {"id":3,"city":"Mistrató","country":"Colombia"},
#    {"id":4,"city":"Ouro Branco","country":"Brazil"},
#    {"id":5,"city":"Ancahuasi","country":"Peru"},
#    {"id":6,"city":"Cartagena","country":"Colombia"},
#    {"id":7,"city":"Maras","country":"Peru"},
#    {"id":8,"city":"Peñaflor","country":"Chile"},
#    {"id":9,"city":"Pilcaniyeu","country":"Argentina"},
#    {"id":10,"city":"Abreu e Lima","country":"Brazil"},
#    {"id":11,"city":"Mucuri","country":"Brazil"},
#    {"id":12,"city":"Iberia","country":"Peru"},
#]    

#paises = set()

#for pais in ciudades:
#    paises.add(pais["country"])
#print(len(paises))

#contrasena = "gera 12"

#valor_ingresado = input("ingrese contrasena:")
#while (valor_ingresado != contrasena):
#    valor_ingresado = input("error vuelva a intentar:")    

#print("ingreso al sistema")

numero = int(input("ingrese el numero:"))

i = 1

while (i < numero):
    if ( i > 10):
        break
    print(i)
    
    i += 1

print("se termino la ejecucion") 