usuario = input("Ingrese el nombre del usuario: ")

if len(usuario) > 5 and len(usuario) < 15 and usuario[0].isalpha() and usuario.isalnum():
    print("Nombre valido")
elif len(usuario) <= 5 or len(usuario) >= 15:
    print("Error: la longitud debe estar entre 6 y 14 caracteres.")
else:
    print("Error: El usuario debe ser alfanumerico y comenzar con una letra.")    