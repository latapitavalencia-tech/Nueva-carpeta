#---Pedir al usuario que ingrese el numero de la tarjeta---
num_tarjeta = input("Por favor, ingrese el numero de su tarjeta de credito: ") #tipo string

#1234 2345 3456 5678

#print("**** **** ****" , num_tarjeta[12:16])
#---Determinar la longitud del numero de la tarjeta---

longitud = len(num_tarjeta) #tipo int
#print(num_tarjeta[longitud-4:longitud])

print("*" * (longitud -4)+ num_tarjeta[longitud-4:longitud])

