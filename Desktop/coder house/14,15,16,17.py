#class 14
#class Personsa ():
#    def __init__(self, nombre , apellido, edad, dni ):
#        self.nombre = nombre 
#        self.apllido = apellido
#        self.edad =  edad
#        self.dni =  dni
#    def saluda(self):
#        return f"me llamo {self.nombre} {self.apllido}"

#class Empleado (Personsa):
#    def __init__(self, nombre, apellido, edad, dni, sueldo, horario):
#        super().__init__(nombre, apellido, edad, dni)
#        self.sueldo =  sueldo
#        self.horario =  horario

#    def fichar(self, ingreso):
#        if ingreso < self.horario:
#            return f"llegue {self.horario - ingreso} minutos temprano"
#        else:
#            return f"llegue {self.horario - ingreso} minutos tarde"
#class Seguridad (Empleado):
#    def __init__(self, nombre , apellido, edad, dni, sueldo , horario, vehiculo, arma ):
#        super().__init__(nombre , apellido, edad, dni, sueldo , horario)
#        self.vehiculo = vehiculo
#        self.arma = arma

#    def llamar_policia(self, mensaje):
#        return f"llamo a la policia y digo el  {mensaje}"

#personal = Personsa ("maurico", "cuello", 31 , 123456)
#empleado1 = Empleado ("pepe", "argento", 55, 556677, 10000, 360) 
#seguridad1 = Seguridad ("lionel", "messi", 35, 1234567, 10000, 400, "vW", 22)

#print(seguridad1.saluda())

#classs_15

#import sys

#print("hola mundo")

#print(sys.argv)

import func_mate

print(func_mate.suma(10,20))