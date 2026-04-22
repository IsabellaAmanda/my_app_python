### Class ###
class FirtsClases():#CamelCase
    def __init__(self):
        pass #Es como none sirve para rellenar en donde no hay bloque
    
#print(FirtsClases)
#print(FirtsClases())

class MyPerson():
    def __init__(self, name, surname):#constructor de clases
        self.name = name
        self.surname = surname
    
    def __str__(self): # representacion en texto
        return f"{self.name} {self.surname}"
    
class MyPerson2():
    def __init__(self, name, surname, nickname = ""):#constructor de clases
        self.name = name
        self.surname = surname
        #self.__nickname = nickname #privado
        self.nickname = nickname
        self.full_name = f"{name} {surname} {nickname}"
    
    #propiedades
    def __str__(self): # representacion en texto
        return self.full_name
    
    
    def Walk(self):
        return f"{self.full_name} esta caminando en el parque"
    
#Definimos los objetos   
my_pers = MyPerson("Isabella", "Cordero")
print(my_pers)
print(f"{my_pers.name} {my_pers.surname}")

my_person = MyPerson2("Isabella", "Cordero")
print(my_person.full_name)
print(my_person.Walk())

my_other_person = MyPerson2("Isabella", "Cordero", "Isa")
print(my_other_person)

my_other_person.full_name = "Andrea de los Angeles - Fuerza Leona"

print(my_other_person.full_name)

my_values = MyPerson2("Andrea", "Martinez", "Andreita")
my_values.full_name = 2026
print(my_values.full_name)


class MyPerson3():
    def __init__(self, name, surname, nickname = ""):#constructor de clases
        #metodos privados
        self.__name = name #privado
        self.__surname = surname
        self.__nickname = nickname
        self.full_name = f"{name} {surname} {nickname}"
    
    #propiedades
    def __str__(self): # representacion en texto
        return self.full_name
    
    def get_name(self):
        return self.__name
    def Walk(self):
        return f"{self.full_name} esta caminando en el parque"
    
new_values = MyPerson3("Isabella", "Cordero", "Isa")
print(new_values.get_name()) #Isabella