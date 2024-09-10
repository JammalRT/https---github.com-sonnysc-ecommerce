alumnos=[]
def agregarAlumnos(nombre,clave,promedio):
    alumno={
        'nombre':nombre,
        'clave':clave,
    }
    alumno.update({'promedio': promedio})
    alumnos.append(alumno)
    return
agregar='s'
while agregar == 's':
    nombre= input('nombre completo: ')
    clave= input('Cual es tu clave?: ')
    califa1= int(input('cual es la primero calificacion?: '))
    califa2= int(input('cual es la segunda calificacion?: '))
    califa3= int(input('cual es la tercera calificacion?: '))
    promedio = (califa1 + califa2 + califa3)/3
    agregarAlumnos(nombre, clave, promedio)
    agregar=input('Quieres agregar mas alumnos? s/n ')
print(alumnos)