import os
os.system('cls')

print("********** Caracteres de una palabra *********")

palabra = str(input("Ingrese una palabra: "))

def contar_caracteres(cadena):
    contador = 0

    while cadena[contador:]:
        contador += 1
    
    return contador

print("La palabra", palabra, "tiene",contar_caracteres(palabra), "caracteres")