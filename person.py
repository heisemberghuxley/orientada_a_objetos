class Humano:
#atributos
        def __init__(self,nombre,edad,profesion,):
                self.nombre = nombre
                self.edad = edad
                self.profesion = profesion
        def saludar(self):
                print(f"Hola como estas mi nombre es {self.nombre}")
        def como_estoy(self):
                print(f"estoy muy feliz de ser {self.profesion} y tengo {self.edad} años") 

("-------------------------------------------------------------------------")
#(----------------------------------------------)#herencia
class Huxley(Humano):
#atributos
        def __init__(self,nombre,edad,profesion,profesor,cantante):
                super().__init__(nombre,edad,profesion)
                self.profesor = profesor
                self.cantante = cantante
        def soy(self):
                print(f"Soy el mejor {self.profesor}")
        def vocacion(self):
                print(f" y {self.cantante}")
        def como_estoy(self):
                print("fleiz de ser programador")

sandra = Humano("sandra", 24, "programadora")       
huxley = Humano("heisenberg", 25 ,"programador")
huxley.saludar()
print("")
huxley.como_estoy()
print("")
sandra.saludar()
print("")
sandra.como_estoy()

programador = Huxley("huxley","20","programador","full stack","mejor cantante de todos los generos")
programador.como_estoy()
print
programador.saludar()
print()
programador.como_estoy()
print()
programador.soy()
print()
programador.vocacion()

