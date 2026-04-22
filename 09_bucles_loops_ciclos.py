### Loop, Ciclo, Bucles ###

#iterador

# While
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2;#contador incrementa cada 2 
else: # Es opcional
    print("Mi condicion es igual o mayor a 10\n") #solo y ciclo con else se puede hacer en python, un while else (no es comun en otros lenguajes)
    
if my_condition == 10:
    print("Mi condicion es igual a 10")
else:
    print("Mi condicion es mayor o igual a 10\n")
print("La condicion continua\n")


while my_condition < 20:
    my_condition += 1
    
    if my_condition == 15:
        print("Se detiene la ejecucion\n")
        break#al conseguir que la condicion se cumple el break lo que hace es detener la condicion
    print(f"Mi contador = {my_condition}\n")    


print("La ejecucion continua\n")


# For 

my_list = [35, 24, 62, 52, 30, 30, 17] #vamos a recorer los elementos de una lista

print("Una lista\n")
for list in my_list:
    print(f"Elemento {list}\n")

#recorrer los elementos de una tupla
my_tuple = (20, 1.61, "Isabella", "Cordero", "Isabella")

print("Una tupla")
for list in my_tuple:
    print(f"Elemento {list}\n")

#recorrer los elementos de un set
my_set = {"Isabella", "Cordero", 20}

print("Un set\n")
for list in my_set:
    print(f"Elemento {list}\n")
    
#recorrer los elementos de un diccionario
print("Un diccionario")
my_dict = {"Nombre":"Isabella", "Apellido": "Cordero", "Edad": 20, 1:"Python"}

for list in my_dict:
    print(f"Elemento {list}\n")
    if list == "Edad":
        break
else:
    print("El Bucle For para diccionario ha finalizado\n")
    
for list in my_dict.values():
    print(f"Elemento {list}\n")
    if list == "Isabella":
        break
    print("Se ejecuta\n")
else:
    print("El bucle For para diccionario ha finalizado\n")
    

for list in my_dict:
    print(f"Elemento {list}\n")
    if list == "Edad":
        continue#me salta una iteracion
    print("Se ejecuta\n")
else:
    print("El Bucle For para diccionario ha finalizado\n")