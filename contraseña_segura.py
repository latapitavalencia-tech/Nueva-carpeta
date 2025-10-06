"""Por motivos de seguridad una contraseña debe tener una vocal en minúscula, dos símbolos
especiales diferentes (pueden ser solo * o #). Dada una contraseña ingresada por el usuario,
comprueba si es una contraseña segura e indícalo por pantalla."""

#---Pedir contraseña al usuario---
password = input(" Introduce una contraseña ")

#---Comprobar si la contraseña es segura---
if ("a" in password) or ("e" in password) or ("I" in password) \
or ("o" in password) or ("u" in password) and ("*" in password) or ("#" in password):
    print("La contraseña es segura")
else:
    print("La contraseña es insegura")

