import os
import math
os.system('cls')

print("******************** Resolver ecuaciones de segundo grado ********************")

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

p = - b
s = b * b - 4 * a * c
s = math.sqrt(s)

x1 = p + s
x1 = x1 / 2

x2 = p - s
x2 = x2 / 2

print("Soluciones:")
print("X1=", x1)
print("X2=", x2)