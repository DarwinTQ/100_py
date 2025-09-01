# 1. Inicializamos el contador antes del bucle
contador = 1

# 2. La condición se comprueba en cada repetición
while contador <= 5:
    print(f"El contador vale: {contador}")
    # 3. ¡MUY IMPORTANTE! Actualizamos el contador dentro del bucle
    # Si olvidamos esta línea, el bucle será infinito.
    contador = contador + 1

print("Fin del programa.")


###########################################
cuenta_atras = 10
while cuenta_atras >= 0:
    print(f'cuenta_atras: {cuenta_atras}')
    cuenta_atras -= 1  # Esto es equivalente a cuenta_atras = cuenta_atras - 1

print("Despegue!!!")