# edad = 20
# tiene_entrada = True

# if edad >= 18:
#     print("Verificación de edad: OK.")
#     # Este 'if' está anidado. Solo se comprueba si la edad es >= 18.
#     if tiene_entrada:
#         print("Verificación de entrada: OK. ¡Bienvenido al concierto!")
#     else:
#         print("No tienes entrada. No puedes pasar.")
# else:
#     print("Eres menor de edad. No puedes entrar.")


# Vamos a crear un sistema de acceso a un club.

# Pide al usuario su edad.

# Pide al usuario si es miembro VIP (puedes pedir que responda "si" o "no").

# La regla principal es que debe ser mayor de edad (18 años o más) para poder entrar.

# Usa un if principal para verificar si el usuario es mayor de edad.

# Si es mayor de edad, usa un if-else anidado para verificar si es miembro VIP.

# Si es miembro VIP, muestra "Bienvenido al club. Tienes acceso a la zona VIP."

# Si no es miembro VIP, muestra "Bienvenido al club. Tienes acceso a la zona general."

# Si es menor de edad, en el else del if principal, muestra "Acceso denegado. Debes ser mayor de edad para entrar."
# Pide al usuario su edad y la convierte a número entero.
edad = int(input("Ingresa tu edad: "))

# Pide al usuario si es miembro VIP y convierte la respuesta a minúsculas.
es_vip = input("¿Eres miembro VIP? (responde si o no): ").lower()

# 1. El if principal verifica si el usuario es mayor de edad.
if edad >= 18:
    # 2. El if-else anidado verifica si es miembro VIP.
    if es_vip == "si":
        # Mensaje para miembros VIP mayores de edad.
        print("Bienvenido al club. Tienes acceso a la zona VIP.")
    else:
        # Mensaje para no miembros VIP mayores de edad.
        print("Bienvenido al club. Tienes acceso a la zona general.")
else:
    # 3. Mensaje si es menor de edad.
    print("Acceso denegado. Debes ser mayor de edad para entrar.")