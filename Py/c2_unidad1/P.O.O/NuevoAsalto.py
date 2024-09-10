from time import sleep
from tqdm import tqdm
class Personaje:
    def __init__(self, nombre, sexo, arma, vida):
        self.nombre = nombre
        self.sexo = sexo
        self.arma = arma
        self.vida = vida
    def asalto (self, otra_personaje):
        print('')
        print('''=== Kevin es un soldado con tenis que camina bastante tranquilo por una 
    calle obscura, hasta que de pronto lo intentan asaltar: ===''')
        print('')
        print(self.nombre+': Ya se la sabe mi '+otra_personaje.nombre+' Celular y Cartera')
        print('')
        print('El',otra_personaje.nombre+': * Se sorprende y le pone un buen putazo *')
    def contra(self, correr, golpear, accion_arma, acercarse, alejarse):
        self.correr = correr
        self.golpear = golpear
        self.accion_arma = accion_arma
        self.acercase = acercarse
        self.alejarse = alejarse     
def run():
    Kevin = Personaje('Kevin','Hombre','navaja',150)
    Sergio = Personaje('Sergio', 'Hombre','Pistola',100)
    Sergio.asalto(Kevin)
    Kevin.contra('Corre detras de ', 10, 100, 'Se acerca a el rapidamente', 'Alcanza a')
    Sergio.contra('huye epicamente de', 10, 50, 'Se le acerca', 'se vio lento y es alcanzado por')
    VidaSer = Sergio.vida
    VidaSerG = VidaSer - Kevin.golpear
    print('')
    print('=== La vida de',Sergio.nombre,'A bajado a:',VidaSerG,'%','===')
    for i in tqdm(range(100)):
        sleep(0.0000001) 
        if i == 90:
            break
    print('')
    print(Sergio.nombre+': Nmms *',Sergio.correr,Kevin.nombre,'*')
    print('')
    print('El',Kevin.nombre+': * '+Kevin.correr+Sergio.nombre,'*')
    print('')
    print('=== El Kevin',Kevin.acercase,'===')
    print('')
    print('=== Sergio',Sergio.alejarse,Kevin.nombre,'===')
    print('')
    print(Sergio.nombre,': * Le dispara a kevin *')
    print('')
    print('=== Pero Kevin por su profecion traia un chaleco antibalas ===')
    print('')
    print('=== Chaleco de kevin se a roto ===')
    for i in tqdm(range(150)):
        sleep(0.0000001) 
        if i == 100:
            break
    print('')
    print('El',Kevin.nombre+': Ya valiste Vrg compa')
    print('')
    print(Kevin.nombre,': * Navajea mortalmente a Sergio *')
    print('')
    print('=== La vida de sergio a sido reducida a 0% ===')
    for i in tqdm(range(100)):
        sleep(0.0000001) 
        if i == 1:
            break
    print('===',Sergio.nombre,'a muerto ===')
    print('')
    print('======  ===  ===    ===')
    print('||      | |  | \\   | |')
    print('||      | |  |  \\  | |')
    print('|====   | |  | | \\ | |')
    print('||      | |  | |  \\| |')
    print('||      | |  | |   \\ |')
    print('||      | |  | |    \\|')
    print('==      ===  ===    ===')
if __name__ == '__main__':
    run()