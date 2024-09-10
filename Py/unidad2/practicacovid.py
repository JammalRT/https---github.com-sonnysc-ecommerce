print('Esta es la prueba de covid')
print('')
iniciar = input('Quieres iniciar? (si/no) ')
print('')
if iniciar == 'si':
    sintoma1 = input('Tienes tos? (si/no) ')
if sintoma1 == 'si':
    sintoma1 = 20
else:
    sintoma1 = 0 
        
sintoma2 = input('Tienes dolor de garganta? (si/no) ')
if sintoma2 == 'si':
    sintoma2 = 20
else:
    sintoma2 = 0
    
sintoma3 = input('Tienes nauseas? (si/no) ')
if sintoma3 == 'si':
    sintoma3 = 20
else:
    sintoma3 = 0

sintoma4 = input('Tienes cuerpo cortado? (si/no) ')
if sintoma4 == 'si':
    sintoma4 = 20
else:
    sintoma4 = 0    

sintoma5 = input('Perdiste el olfato? (si/no) ')
if sintoma5 == 'si':
    sintoma5 = 20
else:
    sintoma5 = 0
    
if sintoma1+sintoma2+sintoma3+sintoma4+sintoma5 > 50:
    print('')
    print('Quedate en casa')
    print('')
    print('Probablilidad de Covid es mas del 50%')
    print('')
elif sintoma1+sintoma2+sintoma3+sintoma4+sintoma5 < 50:
    print('')
    print('Es una gripa normal')
    print('')