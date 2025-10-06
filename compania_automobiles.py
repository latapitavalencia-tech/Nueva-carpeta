#---Preguntar al usuario cuántos autos de cada modelo se vendieron---
rbm_serie1_vendidos =int(input("¿Cuántos RBM Serie 1 se vendieron? "))
rbm_plus_vendidos =int(input("¿Cuántos RBM Serie plus se vendieron? "))
rbm_todoterreno_vendidos =int(input("¿Cuántos RBM Serie todoterreno se vendieron? "))

#---Guardamos los precios de cada modelo en variables---
precio_rbm_serie1 = 20000
precio_rbm_plus = 35000 
precio_rbm_todoterreno = 60000

comision_rbm_serie1 = 0.03
comision_rbm_plus = 0.05
comision_rbm_todoterreno = 0.07


#---Calcular la cantidad de euros a comisionar este mes---

ganancia_rbm_serie1 = rbm_serie1_vendidos * precio_rbm_serie1 * comision_rbm_serie1
ganancia_rbm_plus = rbm_plus_vendidos * precio_rbm_plus * comision_rbm_plus
ganancia_rbm_todoterreno = rbm_todoterreno_vendidos * precio_rbm_todoterreno * comision_rbm_todoterreno

ganancia_total = ganancia_rbm_serie1 + ganancia_rbm_plus + ganancia_rbm_todoterreno

#---Mostrar el resultado por pantalla---
print("La cantidad total de euros a comisionar este mes es de ",ganancia_total," euros.")