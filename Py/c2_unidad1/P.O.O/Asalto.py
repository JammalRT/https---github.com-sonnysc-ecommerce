import random
from time import sleep
from tqdm import tqdm
class Personaje:
    def __init__(self, nombre, sexo, arma, vida):
        self.nombre = nombre
        self.sexo = sexo
        self.arma = arma
        self.vida = vida
    def batalla(self, otra_personaje):
        print('')
        print('''=== Kevin es un soldado con tenis que camina bastante tranquilo por una 
    calle obscura, hasta que de pronto lo intentan asaltar: ===''')
        print('')
        print(self.nombre+': Ya se la sabe mi '+otra_personaje.nombre+' Celular y Cartera')
        print('')
        print('El',otra_personaje.nombre+': * Se sorprende y le pone un buen putazo desatando una pelea callejera *')
    def ataques(self, patada, golpear, accion_arma):
        self.patada = patada
        self.golpear = golpear
        self.accion_arma = accion_arma
def VidaSer(VidaSergio):
    Vida_Sergio.update({'VidaS': VidaSergio})
    for i in tqdm(range(100)):
        sleep(0.0000001) 
        if i == VidaSergio:
            break
def VidaKev(VidaKevin):
    Vida_Kevin.update({'VidaK': VidaKevin})
    for i in tqdm(range(150)):
        sleep(0.0000001) 
        if i == VidaKevin:
            break 
def contraK(VidaKevin):
    print('')
    print('PLOMAZO')
    print('')
    print('=== Tu vida - 25 puntos ===')
    Vida_Kevin.update({'VidaK': VidaKevin})
    for i in tqdm(range(150)):
        sleep(0.0000001) 
        if i == VidaKevin:
            break 
def contraS(VidaSergio):
    print('')
    print('NAVAJAZO')
    print('')
    print('=== Tu vida - 20 puntos ===')
    Vida_Sergio.update({'VidaS': VidaSergio})
    for i in tqdm(range(100)):
        sleep(0.0000001) 
        if i == VidaSergio:
            break
    
Vida_Sergio = {
    
}
Vida_Kevin = {
    
}
soli = 'si'
while soli == 'si':
    Vida_Sergio.update({'VidaS': 100})
    Vida_Kevin.update({'VidaK': 150})
    def run():        
        Kevin = Personaje('Kevin','Hombre','navaja',150)
        Sergio = Personaje('Sergio', 'Hombre','Pistola',100)
        numram = random.randint(149, 150)
        Sergio.batalla(Kevin)
        Kevin.ataques(10, 10, numram)
        Sergio.ataques(10, 10, numram)
        print('')
        selec = input('''Elige a tu personaje: 
1.- Kevin
2.- Sergio

=== ''')
        if selec == '1':
                print('''Seleccionaste a Kevin

Tus accesorios son:
Arma:''',Kevin.arma,'''
Proteccion: Chaleco antibalas
Vida: 150
    ''')        
                print('=== Tu Inicias ===')
                soli2 = 'si'
                while soli2 == 'si':
                    ATK = input('''=== Elige
1.- Patada
2.- Golpe
3.- Navajear

=== ''')
                    if ATK == '1':
                        print('')
                        print('PATADA')
                        print('')
                        VidaSergio = int(Vida_Sergio['VidaS'] - Kevin.patada)
                        print('=== La vida de sergio - 10 puntos ===')
                        VidaSer(VidaSergio)
                        print('Sergio contrataca con Plomo')
                        VidaKevin = int(Vida_Kevin['VidaK'] - Sergio.accion_arma)
                        contraK(VidaKevin)
                        if VidaSergio >=1:
                            print('')
                            print('Sergio Sigue Vivo')
                            print('')
                            soli2 = 'si'      
                        elif VidaSergio == 0:
                            print('')
                            print('Sergio Ya Esta Muerto')
                            print('')
                            soli2 = 'no'
                    elif ATK == '2':
                        print('')
                        print('GOLPE')
                        print('')
                        VidaSergio = int(Vida_Sergio['VidaS'] - Kevin.golpear)
                        print('=== La vida de sergio - 10 puntos ===')
                        VidaSer(VidaSergio)
                        print('Sergio contrataca con Plomo')
                        VidaKevin = int(Vida_Kevin['VidaK'] - Sergio.accion_arma)
                        contraK(VidaKevin)
                        if VidaSergio >=1:
                            print('')
                            print('Sergio Sigue Vivo')
                            print('')
                            soli2 = 'si'      
                        elif VidaSergio == 0:
                            print('')
                            print('Sergio Ya Esta Muerto')
                            print('')
                            soli2 = 'no'
                    elif ATK == '3':
                        print('')
                        print('NAVAJAZO')
                        print('')
                        VidaSergio = int(Vida_Sergio['VidaS'] - Kevin.accion_arma)
                        print('=== La vida de sergio - 20 puntos ===')
                        VidaSer(VidaSergio)
                        print('Sergio contrataca con Plomo')
                        VidaKevin = int(Vida_Kevin['VidaK'] - Sergio.accion_arma)
                        contraK(VidaKevin)
                        if VidaSergio >=1:
                            print('')
                            print('Sergio Sigue Vivo')
                            print('')
                            soli2 = 'si'      
                        elif VidaSergio == 0:
                            print('')
                            print('Sergio Ya Esta Muerto')
                            print('')
                            soli2 = 'no'
                        
                    
        elif selec == '2':
                print('''Seleccionaste a Sergio

Tus accesorios son:
Arma:''',Sergio.arma,'''
Proteccion: Ninguna
Vida: 100
''')      
                print('=== Tu Inicias ===')
                soli2 = 'si'
                while soli2 == 'si':
                    ATK = input('''=== Elige
1.- Patada
2.- Golpe
3.- Disparar

=== ''')
                    if ATK == '1':
                        print('')
                        print('PATADA')
                        print('')
                        VidaKevin = int(Vida_Kevin['VidaK'] - Sergio.patada)
                        print('=== La vida de Kevin - 10 puntos ===')
                        VidaKev(VidaKevin)
                        print('Kevin contrataca con Navajazo')
                        VidaSergio = int(Vida_Sergio['VidaS'] - Kevin.accion_arma)
                        contraS(VidaSergio)
                        if VidaKevin >=1:
                            print('')
                            print('Kevin Sigue Vivo')
                            print('')
                            soli2 = 'si'       
                        elif VidaKevin == 0:
                            print('')
                            print('Kevin Ya Esta Muerto')
                            print('')
                            soli2 = 'no'
                    elif ATK == '2':
                        print('')
                        print('GOLPE')
                        print('')
                        VidaKevin = int(Vida_Kevin['VidaK'] - Sergio.golpear)
                        print('=== La vida de Kevin - 10 puntos ===')
                        VidaKev(VidaKevin)
                        print('Kevin contrataca con Navajazo')
                        VidaSergio = int(Vida_Sergio['VidaS'] - Kevin.accion_arma)
                        contraS(VidaSergio)
                        if VidaKevin >=1:
                            print('')
                            print('Kevin Sigue Vivo')
                            print('')
                            soli2 = 'si'       
                        elif VidaKevin == 0:
                            print('')
                            print('Kevin Ya Esta Muerto')
                            print('')
                            soli2 = 'no'
                    elif ATK == '3':
                        print('')
                        print('PLOMAZO')
                        print('')
                        VidaKevin = int(Vida_Kevin['VidaK'] - Sergio.accion_arma)
                        print('=== La vida de Kevin - 25 puntos ===')
                        VidaKev(VidaKevin)
                        print('Kevin contrataca con Navajazo')
                        VidaSergio = int(Vida_Sergio['VidaS'] - Kevin.accion_arma)
                        contraS(VidaSergio)
                        if VidaKevin >=1:
                            print('')
                            print('Kevin Sigue Vivo')
                            print('')
                            soli2 = 'si'       
                        elif VidaKevin == 0:
                            print('')
                            print('Kevin Ya Esta Muerto')
                            print('')
                            soli2 = 'no'
                            
    if __name__ == '__main__':
        run()
        soli = input('Quires reiniciar? si/no: ')
    

print('')
print('======  ===  ===    ===')
print('||      | |  | \\   | |')
print('||      | |  |  \\  | |')
print('|====   | |  | | \\ | |')
print('||      | |  | |  \\| |')
print('||      | |  | |   \\ |')
print('||      | |  | |    \\|')
print('==      ===  ===    ===')