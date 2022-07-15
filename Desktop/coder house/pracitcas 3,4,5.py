nombre = input("ingrese su nombre:")
edad = int(input("ingrese su edad:")

confirmacion = nombre != "****" and (10 < edad < 18) and (3 <= len(nombre) < 10) and (edad * 4) > 40)

print(confirmacion)
