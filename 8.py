# ¿Es mayor de edad Y vive en la ciudad?
es_mayor = True
vive_ciudad = False
puede_votar = es_mayor and vive_ciudad # Resultado: False (porque una es False)
print(f"¿Puede votar?: {puede_votar}")

# ¿Es mayor de edad Y vive en la ciudad?
# ¿Tiene descuento por ser estudiante O por ser de la tercera edad?
es_estudiante = False
es_tercera_edad = True
tiene_descuento = es_estudiante or es_tercera_edad # Resultado: True (porque una es True)
print(f"¿Tiene descuento?: {tiene_descuento}")

esta_lloviendo = False
podemos_salir = not esta_lloviendo # Resultado: True
print(f"¿Podemos salir?: {podemos_salir}")

#---------------------
age = int(input("¿Cuántos años tienes?: "))  # Pedimos al usuario que ingrese su edad
height = float(input("¿Cuánto mides en metros?: "))  # Pedimos al usuario que ingrese su altura

mayor_a10 = age > 10
mayor_a160 = height > 1.60
puede_subir = mayor_a10 and mayor_a160  # Puede subir si es mayor a 10 años y mide más de 1.60 metros
print(f"¿Puede el usuario subir a la atracción?: {puede_subir}")  # Imprimimos si puede subir o no
