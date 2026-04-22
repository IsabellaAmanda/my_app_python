### Dictionaries in Python ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# {key: value}
#inicializar diccionario con datos
my_other_dict = {
    "Nombre": "Isabella",
    "Apellido": "Cordero",
    "Edad": 20,
    1: "Python"}

print(len(my_other_dict))

my_dict = {
    "Nombre": "Isabella",
    "Apellido": "Cordero",        
    "Edad": 20, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.61
    }

print(my_dict)
print(my_other_dict)

# Longitud del diccionario
print(len(my_other_dict))
print(len(my_dict))

# Acceder a los elementos por su clave
print(my_dict["Nombre"])

# Modificar los elementos
my_dict["Nombre"] = "Alejandra"
print(my_dict["Nombre"])

# Acceder a un valor usando una clave numérica
print(my_dict[1])

# Agregar nuevos elementos
my_dict["Address"] = "Calle Luna Calle Sol"
print(my_dict)

# Eliminar elementos
del my_dict["Address"]
print(my_dict)

# Verificar si una clave o valor existe
print("Apellido" in my_dict)
print("Isabella" in my_dict.values()) 
print("Corderito" in my_dict.values())
print(my_dict.get("Apellido"))

#funciones de los diccionarios para obtener sus elementos
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
my_new_dict = my_other_dict.fromkeys(("Nombre", 1)) # crea un nuevo diccionario con las claves especificadas y valores None
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", "Edad"), "Desconocido") # crea un nuevo diccionario con las claves especificadas y valores "Desconocido"
print(my_new_dict)

my_list = ["Nombre", "1", "Desconocido"]
my_new_dict = dict.fromkeys((my_list)) # crea un nuevo diccionario con las claves especificadas en la lista y valores None
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1), "Desconocido") # crea un nuevo diccionario con las claves especificadas en la cadena y valores 1
print(my_new_dict)

#my_new_dict = dict.fromkeys(my_dict, ("Cordero", "Amanda"))
#print(my_new_dict)

#my_new_dict = dict.fromkeys(my_dict, my_dict)
#print((my_new_dict))

#my_new_dict = dict.fromkeys(my_dict, ["Isabella", "Cordero"])
#print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(list(my_new_dict.values()))
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))


