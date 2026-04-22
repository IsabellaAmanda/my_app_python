### Conditionals ###

my_condition = True

if my_condition: #Es lo mismo if my_condition == True
    print("This is a nigga 👩🏿‍🦰👱🏿‍♂️\n")
    if my_condition:
        print("This is Asia 🙆\n")#Es lo mismo if my_condition == True
        
my_condition = 5 * 2
if my_condition == 10:
    print("Sabes contar carajito pajuo 👱🏻\n")
    

answer = int(input("Cuanto es (5 * 2)?\n"))

#condicional doble 
if my_condition == answer:
    print("Volviste, chico, no eres mente pollo 👱🏻‍♂️🐥\n")
else:
    print("Chico, espavila vale 🦎 \n")
    
my_new_condition = int(input("Adivina el rango:\nEscribe cualquier numero\n"))

if my_new_condition > 10 and my_new_condition < 20:
    print("Goob job. This is a correct answer\n")
   
my_answer = "Negro"

respuesta = input("Cual es el tu color favorito?\n")

if my_answer == respuesta:
    print("Respuesta correcta\n")
else:
    print("Pajuo, responde bien\n")
    
print("La ejecucion continua\n")

condition = 5 * 3

# Elif

if condition > 10 and condition < 20:
    print("Cumple con la condicion\n")
elif condition == 15:
    print("Sigue cumpliendo con la condicion\n")
else:
    print("No cumple ninguna de las condiciones")

#condicionales anidados
edad = int(input("Ingresa tu edad: "))
estudiante = input("¿Eres estudiante? (s/n): ")

if edad >= 18:
    # Primera condición
    if estudiante.lower() == 's':
        # Condición anidada dentro del primer if
        print("Eres mayor de edad y estudiante.")
    else:
        print("Eres mayor de edad pero no estudiante.")
else:
    print("Eres menor de edad.")

cantidad = int(input("Cuantos Cupcakes quieres?\n"))
is_student = input("Eres estudiante (s-n)?\n")
price = 348.76

if cantidad >= 5:
    if is_student.lower() == 's':
        descount = 0.25
    elif is_student.lower() == 'n':
        descount = 0.05
    else:
        descount = 0.0
else:
    print("No compro nada. Dios me lo bendiga\n")
    descount = 0.0

total =  (price*cantidad) 
total_price = total - (total * descount) 
print("Gracias por su compra el total es: %.2f Bs" %(total_price))
  
my_string = "Mi cadena de texto"

if not my_string:
    print("Mi cadena no esta vacia")#input nunca devuelve vacia si no, ""
    
my_string = input("Ingresa una frase:\n")

if my_string == "Mi cadena de texto":
    print("Mis cadenas coincideen\n")
elif my_string == "":
    print("Conio esta vacio, valee\n")
else:
    print("Comentario Ramdon XD\n")

 