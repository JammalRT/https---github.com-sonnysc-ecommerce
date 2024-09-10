def busqueda_lineal(calificaciones, redondeo):
    for i in range(len(calificaciones)):
        if calificaciones[i] == redondeo:
            return i
    return -1
calificaciones = []
for i in range(10):
    num = int(input("Ingresa la calificacion: "))
    calificaciones.append(num)
promedio = sum(calificaciones) / len(calificaciones)
redondeo = round(promedio)
print('')
print("Promedio de:", redondeo)
i = busqueda_lineal(calificaciones, redondeo)
if i != -1:
    print('')
    print("El promedio se encuentra en la posicion", i+1, "de la lista.")
else:
    print('')
    print("El promedio no se encuentra en el arreglo.")
print('')