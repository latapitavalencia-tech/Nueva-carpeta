#pedir nombre de usuario
#print("¿Como te llamas?")
#nombre = input()
nombre = input("¿Como te llamas? ")

#---reformater nombre---
nombre = nombre.replace(".","")
lenguaje = "python"
#---escribimos mensaje en una variable---
mensaje = "Hola, " + nombre.title() + ",estas usando "+ lenguaje.title() + "!"
#imprimimos el mensaje por pantalla
print(mensaje)