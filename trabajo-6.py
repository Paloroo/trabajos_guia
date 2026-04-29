archivo = input("Ingrese el nombre de su archivo: ").lower()

if archivo.endswith(".jpg") or archivo.endswith(".png") or archivo.endshith(".gif"):
    print("El archivo es una imagen.")
elif archivo.endswith(".pdf") or archivo.endswith(".doc"):
    print("El archivo es un documento.")
else:
    print("Tipo de archivo desconocido.")    