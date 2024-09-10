carro = {'marca': 'BMW',
         'modelo': '2022',
         'color' : 'rojo'
}

solisitar = 'si'
while solisitar == 'si':
    preg = input('que quiere conocer del veiculo? ')
    if preg == 'modelo':
        print('')
        print(carro['modelo'])
        print('')
    elif preg == 'marca':
        print('')
        print(carro['marca'])
        print('')
    elif preg == 'color':
        print('')
        print(carro['color'])
        print('')