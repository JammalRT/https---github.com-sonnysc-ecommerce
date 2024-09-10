datos = [
    {
        'carrera':'ISW',
        'Materia':'Algoritmos',
        'Ciclo':'2022-3'
    },
    {
        'carrera':'LAGE',
        'Materia':'Finanzas',
        'Ciclo':'2022-3'
    },
]
for dato in datos:
    if dato['carrera'] == 'ISW':
        dato.update({'edificio':'UD2 Planta alta'})
    else:
        dato.update({'edificio':'UD2 Planta baja'})
    print(dato)