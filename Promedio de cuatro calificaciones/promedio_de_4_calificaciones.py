import os
os.system('cls')

print("************************* Promedio de 4 notas *************************")

a = float(input("Ingrese la primera nota: "))
b = float(input("Ingrese la segunda nota: "))
c = float(input("Ingrese la tercera nota: "))
d = float(input("Ingrese la cuarta nota: "))

e = a + b + c + d
e = e / 4
print("El promedio es:", e)