"""Crea un script que dado un número y una potencia compruebe si ese numero elevado a esa
potencia es par o impar. (Pista: los números pares tiene resto = 0 al dividirlos por 2)
"""
#---Pedir un numero al usuario---
numero = input("Introduce un numero") #es un string,cambiamos a int.
numero = int(numero) #ya es un int

#---Comprobar si el nuemero es par o impar---
if numero % 2 == 0:
    print("El numero",numero,"es par")
else:
    print ("El numero",numero,"es impar")
#Si el numero es multiplo a dos es par
#Si no es multiplo a dos sera impar
