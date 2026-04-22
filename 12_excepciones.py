#Exceptions  en Python

number, number2 = 10, 5
#number2 = "1"
print(number + number2)


print(number + number2) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

try:
    print(number + number2)
    print("La suma se ha realizado correctamente\n")
except:
    print(f"Se ha producido un error al intentar sumar\n")