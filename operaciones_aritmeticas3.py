#---Pedir al usuario dos numeros enteros---
num1 = int(input("Por favor, introduce un numero entero: "))
num2 = int(input("Por favor, introduce otro numero entero: "))

#---Calcular el cociente y el resto---
cociente = num1 // num2
resto = num1 % num2

#---Mostrar por pantalla numeros de entrada,cociente y resto---
print("Los numeros introducidos son ",num1, "y", num2)
print("El cociente es ", cociente)
print("El resto es ", resto)    