correo = input("Ingrese su correo: ").strip()

if correo.count("@") == 1 and not  correo.startswith("@") and (correo.endswith(".com") or correo.endswitch(".org")):
    print("Correo valido.")
elif correo.count("@") != 1:
    print("Error: El correo debe contener exactamente un '@' .")
else:
    print("Error: El correo debe terminar en '.com' o '.org' y no empezar con '@'.")