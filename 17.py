# code 17
# Vamos a imprimir solo los números impares del 1 al 10
for numero in range(1, 11):
    # Si el número es par...
    if numero % 2 == 0:
        # ...saltamos esta vuelta y vamos a la siguiente.
        continue
    
    # Esta línea solo se ejecuta si el 'continue' no se activó (es decir, si el número es impar).
    print(numero)