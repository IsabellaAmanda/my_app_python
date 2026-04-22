### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)  

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)  

# Formateo
name, surname, age = "Isabella", "Cordero", 20
print("Mi nombre es %s %s y tengo %d" %(name, surname, age))
print("Mi nombre es {} {} y tengo {}". format(name, surname, age))
print("Mi nombre es" + name + " " + surname + "y mi edad es" + str(age))
print(f"Mi nombre es {name} {surname} y tengo {age}") # F"Strings

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)

# Division
langueges_slice = language[1:3]
print(langueges_slice)

langueges_slice = language[1:]
print(langueges_slice)

langueges_slice = language[-2]
print(langueges_slice)

langueges_slice = language[0:6:2]
print(langueges_slice)

#Reverse

reverse_languege = language[::-1]
print(reverse_languege)

#Funciones del sistema

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))
print(language.startswith("Py"))



