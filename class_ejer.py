
class Student():
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
     
    def Student_info(self):
        #info = f"Name: {self.name}\nAge: {self.age}\nMajor: {self.major}"
        #return info
        print("Estudiando...")
    
    
name = input("Ingrese el nombre del estudiante:\n")
age = input("Ingrese la edad del estudiante:\n")
major = input("Ingrese la carrera del estudiante:\n")

student1 = Student(name, age, major)

info = f"""DATOS DEL ESTUDIANTE \n 
       Nombre: {student1.name}\n 
       Edad: {student1.age}\n 
       Grado Academico: {student1.major}\n"""

print(info)


while True:
    
    print("¿Qué desea hacer? (Escriba 'estudiar' para continuar o 'salir' para terminar)")
    Student = input()
    if Student.lower() == "estudiar":
        student1.Student_info()
    elif Student.lower() == "salir":
        print("Saliendo del programa...")
        break