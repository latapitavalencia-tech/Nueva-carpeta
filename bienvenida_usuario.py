"""Un ordenador tiene tres usuarios distintos (Alejandro, Naomi y Sergio) y otro usuario invitado.
Haz un script que pida el nombre al usuario y le dé una bienvenida personalizada. Crea el script
de tal manera que si el usuario no es ninguno de los tres se le dé un saludo genérico.
¿Que ocurre si uno de los usuarios introduce su nombre completamente en minúsculas?¿Y si lo
introduce en mayúsculas? ¿Y si sin querer pone in punto en mitad de su nombre (p.e. nao.mi)?¿Y
si se le cuela una almohadilla (p.e se#rgio)?"""
#---Pedir nombre por pantalla---
nombre = input("Introduce tu nombre de usuario")
usuario_1 = "alejandro"
usuario_2 = "naomi"
usuario_3 = "sergio"
#---Variables con los nombres de los usuarios---

#---Comprobar si el nombre coinside con el de usuario---
#Si coinside entonces damos bienvenida al usuario
if nombre.lower() == usuario_1 or nombre.lower() == usuario_2 or nombre.lower() == usuario_3:
    print("Bienvenido",nombre.title(),"!")
#Si no damos bienvenida generica
else:
    print("Bienvenido usuario invitado!")

