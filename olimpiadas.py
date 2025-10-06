#---Pedimos los tiempos por pantalla---
tiempo_Hannah=input("Ingresa el tiempo de Hannah Neise(formato: minutos segundos centesimas): ")
tiempo_Jackie=input("Ingresa el tiempo de Jackie Narracott(formato: minutos segundos centesimas): ")
tiempo_Kimberley=input("Ingresa el tiempo de Kimberley Bos(formato: minutos segundos centesimas): ")
#---Extraer minutos segundos y centesimas---
minutos_Hannah, segundos_Hannah, centesimas_Hannah = tiempo_Hannah.split(" ")
minutos_Jackie, segundos_Jackie, centesimas_Jackie = tiempo_Jackie.split(" ")
minutos_Kimberley, segundos_Kimberley, centesimas_Kimberley = tiempo_Kimberley.split(" ")
#---Convertimos los tiempos a segundos---
tiempo_Hannah = float(minutos_Hannah) * 60 + float(segundos_Hannah) + float(centesimas_Hannah) *0.01
tiempo_Jackie = float(minutos_Jackie) * 60 + float(segundos_Jackie) + float(centesimas_Jackie) *0.01
tiempo_Kimberley = float(minutos_Kimberley) * 60 + float(segundos_Kimberley) + float(centesimas_Kimberley) *0.01
#---Calculamos velocidad media---
velocidad_Hannah = 100.0 / tiempo_Hannah
velocidad_Jackie = 100.0 / tiempo_Jackie
velocidad_Kimberley = 100.0 / tiempo_Kimberley
#---Mostramos resultados por pantalla---
print("La velocidad de Hannah Neise fue de:" , velocidad_Hannah , "metros por segundo")
print("La velocidad de Jackie Narracott fue de:" , velocidad_Jackie , "metros por segundo")
print("La velocidad de Kimberley Bos fue de:" , velocidad_Kimberley , "metros por segundo")