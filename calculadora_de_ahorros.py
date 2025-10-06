#---Pedir nimbre de usuario---
nombre = input("Por favor, introduce tu nombre: ")

#---Saludar al usuario---
print("Hola ", nombre)

#---Guardamos ingresos y horas trabajadas ---

ingresos_hora = 25 # euros
horas_trabajadas =25 # horas al semana

#---Calculamos la ganancia semanal--

salario_semanal = ingresos_hora * horas_trabajadas

#---Calculamos la ganancia anual---

ganancias_anuales = salario_semanal * 52

#---Imprime ganancia anual---

print(nombre.title(), "tienes unas ganancias anuales de: ", ganancias_anuales, "euro")

#---Pedimos los gastos semanales al usuario---

gastos_semanales = float(input("Por favor, introduce tus gastos semanales: "))

#reduzco los gastos semanales a3/4 de lo anterior

gastos_semanales = gastos_semanales * 3 / 4 

#---Calculamos el gasto anual---    

gasto_anual = gastos_semanales * 52

#---Calculamos el ahorro anual---

ahorro_anual = ganancias_anuales - gasto_anual

print("Tu ahorro anual es de: ", ahorro_anual, "euro")