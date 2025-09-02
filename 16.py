# frase = "Hola"

# # La variable 'letra' tomará el valor 'H', luego 'o', luego 'l', y finalmente 'a'.
# for letra in frase:
#     print(letra)

##############################

frase = input("Ingresa una frase: ")
contador_vocales =0

for letra in frase:
    if letra.lower() in 'aeiou':
        contador_vocales +=1

print(f"Cantidad de vocales en la frase: {contador_vocales}")