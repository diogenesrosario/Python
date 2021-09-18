import os
os.system('cls')

print("********** Velocidad Promedio *********")

distancia = int(input("Ingrese la distancia en KM: "))
tiempo = int(input("Ingrese el tiempo (Horas): "))

velocidad = distancia / tiempo

print("La velocidad promedio es:",velocidad,"Km/h")