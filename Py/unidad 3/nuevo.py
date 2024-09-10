a = {
    'materia': 'algoritmos',
    'grado': 1,
    'grupo': 'C',
    'carrera': 'ISW'
}

b = {
    'total_alumnos': 31
}
a.update(b)
a.update({'materia':'algoritmos'})

print(a['materia'],a['carrera'])