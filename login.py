"""Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta).
Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe
indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la
contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.
Cambia el script para que no distinga entre mayúsculas y minúsculas.
(Pista: Necesitarás in If Statement anidado)"""
#---Tenemos la contraseña correcta---
key = "micontraseña123"
#---Pedir al usuario la contraseña---
password = input("Introduce la contraseña")
#---Comprobar si la contraseña coincide con nuestra key---
#Si coincide damos bienvenida al usuario
password= password.replace(".","")
if password.lower() == key:
    print("Bienvenido usuario!")
else:
    print("Error,la contraseña es invalida")
    password = input("Introduce la contraseña de nuevo")
    if password.lower() == key:
        print("Contraseña corecta,bienvenido!")
    else:
        print("Error,la contraseña es incorecta")
        print("Cerramos el sistema")



