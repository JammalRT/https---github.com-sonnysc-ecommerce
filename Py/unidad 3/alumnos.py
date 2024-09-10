alumnos = []
def agregarAL(nombre, carrera, grupo):
    alumno = {
        'nombre':nombre,
        'carrera':carrera,
        'grupo':grupo,
    }
    alumnos.append(alumno)
    return alumnos

def acualizarAL(alumnos):
    for alumno in alumnos:
        alumno.update({'edificio':'UD2 Planta alta'})
        return alumnos

def buscar_AL(llave, valor):
    buscar = []
    for alumno in alumnos:
        if alumno[llave] == valor:
            buscar.append(alumno)
    return buscar 

agregar = 's'
while agregar == 's':
    nombre = input('nombre completo: ')
    carrera = input('Carrera: ')
    grupo = input('Grupo: ')
    
    agregarAL(nombre, carrera, grupo)
    agregar = input('Agregar mas alumnos? (s/n) ')

print('alumnos totales')
print(alumnos)
llave = input('porque llave deseas buscar? ')
valor = input('que deseas buscar? ')
print('Alumnos de busqueda')
print(buscar_AL(llave, valor))

afi = input('desea actualezar datos de los alumnos? (s/n) ')
if afi == 's': 
    print(acualizarAL(alumnos))