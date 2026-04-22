#declaracion de las variables (nombrar identificadores)
#Variables
#usamos sneack_case
my_var = "My String variable"
print(my_var)

my_int_var = 5
print(my_int_var)

my_bool_var = False
print(my_bool_var)

my_str_int_var = str(my_int_var)
print(my_str_int_var)
print(type(my_str_int_var))

#concatenacion de variables en el print
print(my_var, my_str_int_var, my_bool_var)
print("Este es el valor de:", my_bool_var)

#Algunas funciones del sistema
print(len(my_var))

#Variables en una sola línea. Cuidado con abusar de esta sintaxis! 
name, surname, alias, age = "Isabella", "Cordero", "Isa", 20
print("Me llamo:",name, surname,". Mi edad es:", age,". Y mi alias es:", alias)

#Ingresar un datos de entrada por teclado (Inputs)
"""
name = input("What is your name:\n")
age = int(input("How old are you?\n"))

print(name)
print(age)

"""
#Python maneja data types dinamicos
# Cambiamos su tipo
name = 20
age = "Isabella"

print(name)
print(age)

#forzamos el tipo?
address: str = "Mi direccion"
address = True
address = 5
address = 1.5


print(type(address))






