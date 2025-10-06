"""Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error.""" 
#---Pedir dos numeros al usuario---
num1 = float(input("Introduce el dividiendo: ")) #es un string,cambiamos a float.
num2 = float(input("Introduce el divisor: ")) #es un string,cambiamos a float.
#--Comprobar si el divisor es 0---
#Si es cero imprime un error
if num2 == 0.0:
    print("Error ,el divisor no puede ser 0")
#Si no es cero hacemos la division
else:
    division = num1 / num2
    print("El resultado de la division es:",division)   
