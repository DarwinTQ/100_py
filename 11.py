
# nota = 85

# if nota >= 90:
#     print("Calificación: A")
# elif nota >= 80:
#     # Este bloque se ejecuta porque (85 >= 90) es False, pero (85 >= 80) es True.
#     print("Calificación: B")
# elif nota >= 70:
#     print("Calificación: C")
# else:
#     print("Calificación: D")


#######
hora = int(input("Ingresa la hora actual (0-23): "))
#Si la hora está entre 6 y 11 (inclusive), muestra "¡Buenos días!".
if 6 <= hora <= 11:
    print("¡Buenos días!")
elif 12 <= hora <= 18:
    print("¡Buenas tardes!")
elif 19 <= hora <= 23:
    print("¡Buenas noches!")
else:
    print("Hora no válida.")
