arreglo = ['frijoles', 'huevos', 'tamales', 'pozole', 'pizza', 'helados']
valor = input() 
for i in arreglo:
    if valor == i:
        print("")
        print(valor+ ' si se encontraron') 
        print("")
    else:
        print(valor + ' no encontrado' )