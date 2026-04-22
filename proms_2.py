from time import time #calcular el tiempo de ejecucion del programa
class PromediosTwo:
    def __init__(self, name, surname, amount):
        self.name = name
        self.surname = surname
        self.amount = amount


Best_student = []
Sum = 0
cont = 0
suma_best = 0
i = 0
start: float = time()#tiempo de inicio del programa
with open("pupils_large.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.strip().split(' ')
        print(data)

        
        student =  PromediosTwo(data[0], data[1], int(data[2]))
        Sum += int(student.amount) #acumulador
        cont += 1 #contador
        

        if int(student.amount) >= 5:
            Best_student.append(student)
            suma_best += int(student.amount)

end: float = time()#tiempo de finalizacion del programa

print("-----Lista de Mejores Estudiantes-----")
for student in Best_student:
    i += 1
    print(f"{str(i)}. {student.name} {student.surname} - Nota:{student.amount}")


print(f"\nTotal de Estudiantes: {cont}")
print(f"\nPromedio de Mejores Estudiantes: ({(suma_best)/len(Best_student):.2f})")
print(f"Tiempo de ejecucion: {end - start:.4f} segundos")