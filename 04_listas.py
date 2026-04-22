### Lists ###

my_list = list()

my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [20, 1.61, "Isabella", "Cordero"]
print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list.count("Cordero"))
print(my_list.count(30))
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(surname)

print(my_list + my_other_list)

print([1, 2, 3, 4])

# Agregar o añadir elementos
my_other_list.append("IsaCodeDisagner")
print(my_other_list)

my_other_list.insert(1, "Grey")
print(my_other_list)


my_other_list[1] = "Blue"
print(my_other_list)

#Eliminar valores de una lista remove(elimina lo indica)
my_other_list.remove("Blue")
print(my_other_list)

my_list.remove(30)
print(my_list)


#operaciones (colas)
print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

# eliminar un elemento con (del) elimina por indice
del my_list[2]
print(my_list)

#Copy hace una copia de los elementos
my_new_list = my_list.copy()
#Clear limpia todo los elementos que tenia en la lista
my_list.clear()
print(my_list)
print(my_new_list)

# voltea los elementos con el uso del reverse() los que estaba en la posicion[0] ahora esta en la pos[2]
my_new_list.reverse()
print(my_new_list)

#Usar Sort para ordenar los elementos de una lista (menor a mayor)
my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

#cambiar el tipo
my_list = "Hello Python"
print(my_list)
print(type(my_list))