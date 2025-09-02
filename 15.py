# 'numero' es una variable temporal que tomará el valor de cada elemento de la secuencia.
# En la primera vuelta valdrá 0, en la segunda 1, y así sucesivamente.
# for numero in range(5):
#     print(f"Vuelta número: {numero}")


######
n = int(input("Ingresa un número entero positivo: "))
i =1
for i in range(11):
    print(f"La multiplicación de :{n} x {i} = {n*i}")