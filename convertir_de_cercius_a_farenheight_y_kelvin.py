import os
os.system('cls')

print("********* Calcular de grado Celsius a Fahrenheit y Kelvin **********")
celsius = float(input("Ingrese la temperatura en grados cercius: "))

kelvin = celsius + 273.15
fahrenheit = 1.8 * celsius +32

print("Su conversión a grados Kelvin:",kelvin,"° K")
print("Su conversión a grados Fahrenheit:",fahrenheit,"° F")