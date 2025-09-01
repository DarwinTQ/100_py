
total = 0

# El bucle while True se ejecuta indefinidamente hasta que se rompa con 'break'.
while True:
    entrada = input("Ingresa el precio del producto (o escribe 'total' para terminar): ")

    if entrada.lower() == 'total':
        break  # Si es "total", el bucle se rompe.

    precio = float(entrada)
    total += precio
   
    print(f"Total acumulado: ${total:.2f}")


print(f"El total de su compra es: ${total:.2f}")