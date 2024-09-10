arreglo = []
arreglo2 = []
solicitar = input('Desea empezar a agregar datos? (si/no) ')
while solicitar == 'si':
    valor = int(input('Escribe el valor: '))
    if valor % 2 == 0:
        arreglo.append(valor)
        solicitar = input('Desea segir agregando valores? (si/no) ')
    else:
        arreglo2.append(valor)
        solicitar = input('Desea segir agregando valores? (si/no) ')
        
pedir = input('Que numeros quieres imprimir? (par/inpar)? ')
if pedir == 'par':
    print(arreglo)
elif pedir == 'inpar':
    print(arreglo2)