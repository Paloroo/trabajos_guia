url = input("Ingrese una URL: ")

if url.startswith("http://") or url.startswith("htpps://"):
    sin_protocolo = url.split("://")[1]
    if "/" in sin_protocolo:
        dominio = sin_protocolo.split("/")[0]
    else:
        dominio = sin_protocolo
    print(f"El dominio es: {dominio}")        
elif url == "":
    print("url vacia")
else:
    print("Error: La URL debe comenzar con http:// o htpps://")    