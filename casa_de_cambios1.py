#---pedir al el usuario que ingrese la cantidad en euros---
euros = input("Ingrese la cantidad de euros que desea convertir: ") #tipo string

#---convrtir la cantidad ingresada de euros de string a float---
euros = float(euros) #tipo float

#---convertir la cantidad de euros en dolares---
dolares = euros * 1.2

#---imprimir el resultado de la conversion---
print("los", euros,"€ son",dolares ,"dolares")