import os
import math
os.system('cls')

print("******** Encontrar el Cateto Faltante ********")

catetoA = int(input("Ingrese un cateto: "))
hipotenusa = int(input("Ingrese la hipotenusa: "))

catetoA = catetoA * catetoA
hipotenusa = hipotenusa * hipotenusa

resta = hipotenusa - catetoA
raiz = math.sqrt(resta)

print("El cateto faltante es: ",raiz)