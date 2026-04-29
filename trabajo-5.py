palabra = input("Ingrese la palabra: ")
palabra_limpia = palabra.replace(" ", "").lower()

if len(palabra_limpia) > 0 and palabra_limpia == palabra_limpia[:: -1]:
    print("Es un palindromo.")
elif len(palabra_limpia) == 0:
    print("Error: Entrada vacia.")
else:
    print("No es un palindromo.")       