"""El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media.
Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. Crea un script que
pida el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no."""

#---Pedir los datos al usuario---
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: ")) #es un string,cambiamos a int.
nota_media = float(input("Introduce tu nota media: ")) #es un string,cambiamos a float.

nombre = nombre.title() #Ponemos el nombre en formato titulo
#---Comprobamos si el estudiande puede optar por la beca---
if (edad >= 17 and edad <=21) and nota_media >=8.0:
    print("El estudiante",nombre, "cumple los requisitos para optar a la beca: ")
else:
    print("El estudiante",nombre," no cumple los requisitos para optar por la beca: ")