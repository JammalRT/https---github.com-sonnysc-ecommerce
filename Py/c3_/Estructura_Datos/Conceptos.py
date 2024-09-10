lista = [34, 56, 912, True, "3B ISW"]

Tupla = [34, 56, 912, True, "3B ISW"]

diccionario = {'papa': 'Mayor',
               'Hermano': 'junior',
               'hijo': 'ricardo'}

segundaLista = [lista, Tupla, diccionario]

estructura = {1:lista,
              2:Tupla,
              3:diccionario}

valor = estructura[1]
print(valor)

valorLista = valor[4]
print(valorLista)

print(type(valorLista))
