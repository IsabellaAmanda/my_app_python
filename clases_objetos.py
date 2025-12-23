#Pascal case

class NombreClase():
    #ATRIBUTOS, constructores
    def __init__(self, marca, modelo, memoria, camara):
        #propiedades o atributos
        self.mar = marca
        self.mod = modelo
        self.mem = memoria
        self.cam = camara
    
    #METODOS es una función dentro de una clase, comportamiento
    def mostrar_info(self):
        #F string
        #self   hace referencia al objeto actual
        info = f"Marca: {self.mar}\nModelo: {self.mod}\nMemoria: {self.mem}\nCámara: {self.cam}"
        return info
    
#crear un objeto de la clase NombreClase
celular1 = NombreClase("Samsung", "Galaxy S21", "128GB", "64MP")
#llamar al método mostrar_info
print(celular1.mostrar_info())  
 
 