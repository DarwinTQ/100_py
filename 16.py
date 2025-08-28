edad = 17

if edad >= 18:
    print("Acceso permitido al área de adultos.")
else:
    # Este bloque se ejecuta porque la condición (17 >= 18) es False.
    print("Acceso denegado. Esta área es solo para mayores de edad.")

#-------------------------------------------------
numero = int(input("Ingresa tu calificación: "))
if numero >60:
    print('¡Felicidades! Has aprobado')
else:
    print('Necesitas estudiar más. Has reprobado.')