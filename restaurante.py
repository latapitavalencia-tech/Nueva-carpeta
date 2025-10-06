#---Definir el precio de cada alimento---
precio_ensalada_mixta = 12
precio_sopa_pescado = 10
precio_dorada_horno = 18
precio_arroz_curry = 14
precio_lasañ_carne = 15
precio_brownie_chocolate = 8
precio_helado = 6
precio_refresco = 5.5
precio_cafe = 3.5

#---Pedir al usuario que introduzca la cantidad de cada alimento que ha consumido---

cantidad_ensalada_mixta = int(input("¿Cuántas ensaladas mixtas ha consumido? "))
cantidad_sopa_pescado = int(input("¿Cuántas sopas de pescado ha consumido? "))
cantidad_dorada_horno = int(input("¿Cuántas doradas al horno ha consumido? "))
cantidad_arroz_curry = int(input("¿Cuántos arroces al curry ha consumido? "))
cantidad_lasañ_carne = int(input("¿Cuántas lasañas de carne ha consumido? "))
cantidad_brownie_chocolate = int(input("¿Cuántos brownies de chocolate ha consumido? "))
cantidad_helado = int(input("¿Cuántos helados ha consumido? "))
cantidad_refresco = int(input("¿Cuántos refrescos ha consumido? "))
cantidad_cafe = int(input("¿Cuántos cafés ha consumido? "))

#---Calculamos el total de la cuenta---

total = cantidad_ensalada_mixta * precio_ensalada_mixta + \
        cantidad_sopa_pescado * precio_sopa_pescado + \
        cantidad_dorada_horno * precio_dorada_horno + \
        cantidad_arroz_curry * precio_arroz_curry + \
        cantidad_lasañ_carne * precio_lasañ_carne + \
        cantidad_brownie_chocolate * precio_brownie_chocolate + \
        cantidad_helado * precio_helado + \
        cantidad_refresco * precio_refresco + \
        cantidad_cafe * precio_cafe

#---Imprimimos la cuenta total por pantalla---
print("El total de su cuenta es de: ", total, " euros.")

