import os
import webbrowser

os.system('cls')

print("********** Crear HTML con nombre y apellido *********")
nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su Apellido: "))

html = f"""
<html>
    
<head><title>Datos</title></head>
<body>

<center>
<h1>Sus Nombre y Apellido es:</h1>    
        <h4>Nombre: {nombre}</h4>
        <h4>Apellido: {apellido}</h4>
</center>
</body>
</html>
    </body>

</html>
"""
nombre_del_archivo = 'Programa_10' +'.html'
archivo = open(nombre_del_archivo,'w')
archivo.write(html)
archivo.close()
os.system('explorer '+nombre_del_archivo)