# 10 dividido entre 3 es 3 con un resto de 1.
resto = 10 % 3  # El resultado es 1

# 12 dividido entre 2 es 6 con un resto de 0.
# Si el módulo de un número entre 2 es 0, el número es par.
es_par = 12 % 2 # El resultado es 0

# 10 dividido entre 3 es 3.333...
division_entera = 10 // 3 # El resultado es 3

# 2 elevado a la potencia de 3 (2 * 2 * 2)
potencia = 2 ** 3 # El resultado es 8
#----------------------------------------
n = 3661
hor = n//60
min = hor%60
seg  = n%60
print(hor)
print(min)
print(seg)
print(f'{n} segundos equivale a {hor} horas, {min} minutos, y {seg} segundos')