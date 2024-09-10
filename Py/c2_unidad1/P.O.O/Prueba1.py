class Persona:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def saluda (self, otra_persona):
        print('hola '+self.nombre+' me llamo '+otra_persona.nombre)
def run():
    Jammal = Persona('Jammal',18)
    Sergio = Persona('Sergio', 24)
    
    Jammal.saluda(Sergio)
    
if __name__ == '__main__':
    run()