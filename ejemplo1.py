"""Crea un script que dado un usuario, le de 
una bienvenida personalizada,si es el administador
y una bienvenida generica si es otra persona"""
#---Pedir al usuario que introdusca su nombre---
nombre = input("Introduce  tu nombre: ")
#Nombre de administrador
administrador = "Alejandro"
#---Comprobar si ese nombre es igual que el del admistrador---
#Si es igual, le damos una bienvenida personalizada
if nombre.lower() == administrador.lower(): # case insensitive
    print("Bienvenido",nombre.title() +  "!")
#Si no, una bienvenida generica
else:
    print("!Bienvenido, invitado!")


