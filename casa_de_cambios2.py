#---pedir al el usuario que ingrese la cantidad en euros---
euros = input("Ingrese la cantidad ede euros que desea convertir: ") #tipo string

#---convrtir la cantidad ingresada de euros de string a float---
euros = float(euros) #tipo float

#---convertir la cantidad de euros en dolares---
dolares = euros * 1.2

#---calculamos la cantidad que se queda la casa de cambios---
tasas_gestion = dolares * 0.1

#---calculamos la cantidad final que recibe el usuario---
dolares_recibidos = dolares-tasas_gestion

#---imprimir el resultado de la conversion---
print( "Monto ingresado: ", euros, " euros")
print("Cambio en dolares: ", dolares, " dolares")
print("Tasa de gestion: ", tasas_gestion, " dolares")
print("Monto final recibido: ", dolares_recibidos, " dolares")
