### Functions ###
##Son subrutinas, que permiten optimizar el codigo y ademas darle mayor legibilidad

def muchacho_marico(): #sin parametros {es como un void}
    print("Si eres marico vale")
    

muchacho_marico()

for i in range(1, 3):
    muchacho_marico()
    print(f"Elemeno {i}")
    

def sum_two_values(num1, num2):#Funcion con retorno {con parametros (argumentos) y devuelve un valor}
    result = num1 + num2
    return result

first_num = int(input("Ingrese el valor del primer numero:\n"))
second_num = int (input("Ingrese el valor del segundo numero:\n"))

new_result = sum_two_values(first_num, second_num)

print(f"El resultado de la suma = {new_result}\n")

result1 = sum_two_values("5", "9")#parametos actuales
result2 = sum_two_values(5, 7)

print(f"Sumas1 = {result1}\n")
print(f"Suma2 = {result2}\n")

def with_return(n1, n2, n3):
    
    max = -1
    if (n1 > max and n1 > n2 and n1 > n3):
        max = n1
    elif (n2 > max and n2 > n3):
        max = n2
    else:
        max = n3
    
    return max

num1 = int(input("Ingrese el primer numero:\n"))
num2 = int(input("Ingrese el segundo numero:\n"))
num3 = int(input("Ingrese el tercer numero:\n"))

num_max = with_return(num1, num2, num3)

print(f"El mayor = {num_max}\n")


def my_name_is(name, surname, years):
    print(f"Mi nombre es:{name} {surname}. Tengo {years} de edad\n")
    
name_is = input("")
surname_is = input("")
years_is = int(input())

my_name_is(name_is, surname_is, years_is)

my_name_is(name = "Isa", surname= "Cordero", years=20 )

def print_texts(*texts):#con apuntador a la direccion de la variable
    i = 0
    for text in texts:
        i += 1
        print(f"Element {str(i)}.{text}")
        
def print_texts_upper(*texts):#con apuntador a la direccion de la variable
    i = 0
    for text in texts:
        i += 1
        print(f"Element {str(i)}.{text.upper()}")
        
print_texts("Hola", "Fronted", "JavaScript", "Conio tengo suenio {esa letra no esta en el teclado en englis}")
print_texts("hey")
print("\n")
print_texts_upper("Hola", "Fronted", "JavaScript", "Conio tengo suenio {esa letra no esta en el teclado en english}")
print_texts_upper("Hello")

