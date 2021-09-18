import abc
import os
os.system('cls')

print("************************* Cifrado César *************************")

texto=input("Ingrese el texto: ")

if texto==texto.upper ():

        abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

else:

        abc= "abcdefghijklmnñopqrstuvwxyz"


k= int(input("Ingrese el valor de desplazamiento: "))

cifrado=""

for c in texto:
    if c in abc:
        cifrado += abc[(abc.index(c)+k%(len(abc)))]
    else:
        cifrado+=c

print("Texto Cifrado: ",cifrado)