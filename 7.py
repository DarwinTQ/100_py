# Comparamos dos números
resultado = 10 > 5  # 10 es mayor que 5, así que 'resultado' será True
print(resultado)

# Podemos guardar el resultado en una variable
son_iguales = "hola" == "Hola" # "hola" no es igual a "Hola" (mayúsculas importan), así que será False
print(f"¿Son los textos iguales?: {son_iguales}")

#------------------------------------------------------
name1 = input("¿How old are you?:  ")  # Pedimos al usuario que ingrese su edad
name2 = input("¿How old are you?:  ")  # Pedimos al usuario que ingrese su edad
n1 = int(name1)  # Convertimos la entrada a un número entero
n2 = int(name2)  # Convertimos la entrada a un número entero
usuario_mayor = n1 > n2
edades_iguales = n1 == n2

print(f"¿Es el primer usuario mayor?: {usuario_mayor}")  # Imprimimos si el primer usuario es mayor
print(f"¿Tienen la misma edad?: {edades_iguales}")  # Imprimimos si ambos usuarios tienen la misma edad 
