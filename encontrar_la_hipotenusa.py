import os
import math
os.system('cls')

print("******** Encontrar la hipotenusa ********")

catetoA = int(input("Ingrese el cateto A: "))
catetoB = int(input("Ingrese el cateto B: "))

catetoA = catetoA * catetoA
catetoB = catetoB * catetoB

suma = catetoA + catetoB
resultado = math.sqrt(suma)

print("El resultado de la hipotenusa es: ",resultado)