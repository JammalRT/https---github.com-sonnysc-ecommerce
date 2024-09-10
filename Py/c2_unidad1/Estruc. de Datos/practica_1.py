class alumnospersonal:
    def __init__(self, nombre = " ",apellido = " ", ncontrol = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.ncontrol = ncontrol
        
    def __str__(self):
        imprimircadena = self.nombre + " " + self.apellido + " " + str(self.ncontrol)
        return self.apellido
    
alumno1 = alumnospersonal(
    "Jammal", 
    "Rodriguez", 
    2203150244)

print(alumno1)
