import os

os.system('cls')

print("********** Crear HTML con los siguientes datos *********")
nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su Apellido: "))
telefono = int(input("Ingrese su telefono: "))

html = f"""
<html>
    
<head><title>Datos</title></head>
<body>

<center>
<h1>Sus datos son:</h1>    
        <h4>Nombre: {nombre}</h4>
        <h4>Apellido: {apellido}</h4>
        <h4>Telefono: {telefono}</h4>
</center>
</body>
</html>
    </body>

</html>
"""
archivo = open('Programa_9'+'.html','w')
archivo.write(html)
archivo.close()