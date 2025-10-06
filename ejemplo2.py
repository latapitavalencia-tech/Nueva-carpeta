"""Pide un numero por pantalla e indica si el numero
es divisible por 3(en el sentido de que la division 
de como resultado un numero entero"""

#---Pedir un numero al usuario---
numero = input("Introduse un numero entero:")
numero = int(numero)

#---Comprobar que el numero es divisible por 3---)

#Si es multiplo de 3 ,indicamos por pantalla
if numero % 3 == 0:
    print("El numero ", numero, " es divisible por 3") #,numero,para que lo imprime por pantalla

#Si no indicamos que no lo es
else:
    print("El numero ", numero, " no es divisible por 3")   
    print("\t Python")