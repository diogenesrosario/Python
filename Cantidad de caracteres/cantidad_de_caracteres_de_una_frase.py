import os
os.system('cls')

print("********** Caracteres de la frase *********")

frase = str(input("Ingrese una frase: "))

def contar_caracteres(cadena):
    contador = 0

    while cadena[contador:]:
        contador += 1
    
    return contador

print("La frase", frase, "tiene",contar_caracteres(frase), "caracteres")