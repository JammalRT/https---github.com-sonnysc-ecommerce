nom_fam = ['Hassam',
           'Josue',
           ['Martha',
            'Reynaldo',
            'Modesta',
            'Arturo'],
           'Aracely',
           'Jael',
           'Jammal',
           'Ximena']

nom_prim = ['Fer',
            'Diego',
            'Noel']

num = [5,2,8,6,7,56,987,26,232,8879,32,59,67,65]


fam = str(input('ingresa nombre del familiar: '))
#.append agrega a la lista el valor que ingresas
nom_fam.append(fam)
#.insert agrega un el valor que quieras en la posicion que deseas
nom_fam.insert(3, 'Crista')
#Recorre la lista y revisa si el valor indicado existe en la lista 
print('Jael' in nom_fam)
#.index te indica el indice
print(nom_fam.index('Jammal'))
print(nom_fam.count('Jammal'))
nom_fam.pop(0)
nom_fam.remove('Aracely')
nom_prim.clear()
nom_fam.extend(nom_prim)
sum_lis = nom_fam + nom_prim
print(sum_lis)
mult_lis = (nom_fam * 3)
print('')
num.reverse()
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print('')
print(mult_lis)
print(len(nom_fam))
print(nom_fam)
print(nom_fam[3])
print(nom_fam[2])

