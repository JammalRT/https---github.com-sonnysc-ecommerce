# Nesesario para crear los numeros aleatorios
import random
# Sirve para crear la barra de vida de los personajes 
from time import sleep
from tqdm import tqdm
# Genera los valores aleatorios para el daño de los personajes 
numram = random.randint(1,100)
numram2 = random.randint(1,100)
# clase del jugador
class Player:
  def __name__(self, name, arma, genero):
    self.name = name
    self.hp = 100
    self.attack = numram
    self.arma = arma
    self.genero = genero

# clase del enemigo
class Enemy:
  def __init__(self, name, arma, genero):
    self.name = name
    self.hp = 100
    self.attack = numram2
    self.arma = arma
    self.genero = genero

# función para simular la pelea
def fight(player, enemy):
  print(player.name + ' se enfrenta a ' + enemy.name)
  print('')
  # Mientras la vida de cualquiera de los 2 
  while player.hp > 0 and enemy.hp > 0:
    player_attack = random.randint(0, player.attack)
    enemy_attack = random.randint(0, enemy.attack)
    player.hp -= enemy_attack
    enemy.hp -= player_attack
    print('')
    print(player.name + ' ataca a ' + enemy.name + ' con: ',player.arma, 'y le quita ' + str(player_attack) + ' puntos de vida')
    print('')
    print('=== Vida del Kevin ===')
    # Estas son las lineas nesesarias para la creacion de la barra de vida progreciva 
    for i in tqdm(range(100)):
      sleep(0.00000001)
      if( i == enemy.hp):
        break
    print('')
    print(enemy.name + ' ataca a ' + player.name + ' con: ',enemy.arma,' y le quita ' + str(enemy_attack) + ' puntos de vida')
    print('')
    print('=== Vida del Sergio ===')
    for i in tqdm(range(100)):
        sleep(0.00000001)
        if( i == player.hp):
            break
  # Si cualquiera de los 2 es <= 0  entonces termina la similacion e imprime el mensaje 
  if player.hp <= 0:
    print('')
    print(player.name + ' ha sido derrotado')
  elif enemy.hp <= 0:
    print('')
    print(enemy.name + ' ha sido derrotado')

# Asignacion de los a tributos a los jugadores
player = Player('El Sergio', 'navaja', 'Hombre')
enemy = Enemy('El kevin', 'pistola', 'hombre')

# inicia la pelea
fight(player, enemy)