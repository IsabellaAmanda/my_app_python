#herencia simple (clase que era de clase padre)
class Persona():
    def __init__(self, name, year, nat):
        self.nm = name
        self.yr = year
        self.nat = nat
    
    def hablar(self):
        print("El ofinista habla mucho...bajale 2")
        
class Employee(Persona):
    def __init__(self,name, year, nat, job, rating, college):
        super(). __init__(name, year, nat)
        self.job = job
        self.rating = rating
        self.college = college
    
    
class Articts():
    def __init__(self, hobby):
        self.hob = hobby
        
    def show_hobby(self):
        print(f"Mi habilidad es : {self.hob}")
        
class JobArticts(Persona, Articts):
    def __init__(self, name, year, nat, hobby, money, buss):
        Persona.__init__(self, name, year, nat)
        Articts.__init__(self, hobby)
        self.money = money
        self.buss = buss
        
    
    def Presentarse(self):
        self.show_hobby()
        return f"Soy {self.nm}, tengo {self.yr} años, soy {self.nat}, gano {self.money} $ y tengo un negocio de {self.buss}."
    
    def __str__(self):
        return f"{self.nm}, {self.yr} años, {self.nat}, hobby: {self.hob}, gana {self.money} $, negocio: {self.buss}"

    
''' 
class Employee(Persona):
    def __init__(self,name, year, nat, job, rating, college):
        super(). __init__(name, year, nat)
        self.job = job
        self.rating = rating
        self.college = college
'''

''' 
class Employee(Persona):
    def __init__(self,name, year, nat, job, money):
        super(). __init__(name, year, nat)
        self.job = job
        self.money = money
        
    def hablar(self):
        print("NOOOOO O SIIIIII")
        return super().hablar()

'''


roberto = JobArticts("Roberto", 43, "venezolano", "cantar", 100000,"Programador")
print(roberto)

print(roberto.Presentarse())  # Método propio

#HERENCIA MULTIPLE

#class PeopleNormal(Persona, Employee):
    

        

