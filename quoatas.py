while True:
    
    name_file = input("Ingrese el nombre del archivo a leer:\n")
    try:
        with open(name_file, "r", encoding="utf-8") as file:
            data = file.read(1)
            print(data)
            data = file.read()
            print(data)
        break
    except IOError:
        print("El archivo no existe o no se puede leer.")
    
authors = []
while True:
    name_author = input("Ingrese el nombre del autor:\n")
    authors.append(name_author)

    adds = input("Desea agregar otro autor ? (si-no)\n")
    if adds == "no":        
        break

for name_author in authors:
    with open("quotes.txt", "a", encoding="utf-8") as file:
        file.write(f"({name_author})\n")

    
with open("quotes.txt", "r", encoding="utf-8") as file:
    datos = file.read()
    print(datos)