from time import time #calcular el tiempo de ejecución del programa


class Promedios():
    def __init__(self, name, surname, amount):
        self.name = name
        self.surname = surname
        self.amount = amount

max_student = []
stud = []
total = 0
count_stud = 0
start_time = time() #tiempo de inicio del programa
with open("pupils_txt.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.split(' ')
        print(data)

        student =   Promedios(data[0], data[1], data[2])
        nota = int(data[2])
        total += nota #acumulador
        count_stud += 1 #contador
        student = Promedios(data[0], data[1], nota)
        stud.append(student)

        if nota >= 5:
            max_student.append(student)
            
            
end_time = time() #tiempo de finalización del programa

print("-----Lista de Estudiantes-----")
for student in stud:
    print(f"{student.name} {student.surname} {student.amount}")

print("\n")
print("-----Mejor Estudiante-----")
for student in max_student:
    print(f"{student.name} {student.surname}")

print(f"\nPromedio: ({total/count_stud:.2f})")
print(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos")