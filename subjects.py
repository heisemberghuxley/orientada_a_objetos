class Materias:
    def __init__(self, programacion, ingles, matematicas):
        self._programacion = programacion
        self.matematicas = matematicas
        self.ingles = ingles
        
    def programar(self):
        self.nose_puede = False
        print(f"In {self._programacion}, {self.ingles} is the normal language, \nas it is the default language of the same.")
        
    def programar_en_matematicas(self):
        self.nose_puede_programar_en_matematicas = True
        print(f"Additionally, {self.matematicas} are used in programming \nfor specific points.")
        
    def get_programacion(self):
        return self._programacion
    
    def set_programacion(self, programacion):
        self._programacion = programacion
    
lenguaje = Materias("programming", "English", "mathematics")
print()
lenguaje.programar()
print()
lenguaje.programar_en_matematicas()
lenguaje.set_programacion("coding")
print(lenguaje.get_programacion())

# Inheritance
# (------------------------------------------------------------)
class Especializacion(Materias):
    def __init__(self, programacion, ingles, matematicas, español, comprension_lectura):
        super().__init__(programacion, matematicas, ingles)
        self.español = español
        self.comprension_lectura = comprension_lectura
        
    def significado(self):
        print(f"{self.español} is a Romance language \nderived from spoken Latin.")
        
    def programar(self):
        print(f"{self.comprension_lectura} helps us to understand\nand comprehend what any written text is trying to say, \nhence the importance of learning it.")
        
idiomas = Especializacion("programming", "mathematics", "English", "Spanish", "reading comprehension")
print()
idiomas.significado()
print()
idiomas.programar()
