nombre = input("Ingrese su nombre: ").strip()

if nombre == "":
    print("Error: El nombre esta vacio.")
elif nombre.islower() or nombre.isupper():
    nombre_formateado = nombre.title()
    print(f"Nombre formateado: {nombre_formateado}")
else:
    print(f"Nombre aceptado tal cual: {nombre}")
    