# Tipos de datos abstractos

class Person():
    name = None
    height = 0.0
    weight = 0.0
    def __init__(self, name, height, weight):
        self.name = name 
        self.height = height
        self.weight = weight
        
    def talk(self, massage):
        print(f'Hola, mi nombre es: {self.name} {massage}')

    def __str__(self):
        #return 'Name: ' + self.name + \
            #' height: ' + str(self.height) + \
            #' weight: ' + str(self.weight)

        return(f'Name: {self.name}, Height:{self.height}, weight{self.weight}')
if __name__ == '__main__':
    JoseLuis = Person('Jose Lusi', 1.74, 90)   
    print(JoseLuis)
    print('')
    JoseLuis.talk('Bienvenidos a la clase')
    print('')
    Ricardo = Person('Ricardo', 1.80, 75)
    print(Ricardo)