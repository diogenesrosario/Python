import os
os.system('cls')

from datetime import date

print("************************* Calculadora de edad *************************")

a = int(input("Ingrese su año de nacimiento: "))
b = int(input("Ingrese el mes de nacimiento: "))
c = int(input("Ingrese el dia de nacimiento: "))

def calculo_de_edad(fecha_nacimiento):
    hoy = date.today()
    result = hoy.year - fecha_nacimiento.year
    result -= ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return result
    
nacio = date(a, b, c)
edad = calculo_de_edad(nacio)

print("Su edad es", edad,"años")