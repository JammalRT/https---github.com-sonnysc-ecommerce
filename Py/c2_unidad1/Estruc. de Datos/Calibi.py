calificaciones = []
for i in range(10):
    num = int(input("Ingresa la calificacion: "))
    calificaciones.append(num)
promedio = sum(calificaciones) / len(calificaciones)
redondeo = round(promedio)
print('')
print("Promedio de:", redondeo)
cali_ordenado = sorted(calificaciones)
izquierda = 0
derecha = len(cali_ordenado) - 1
encontrado = False
while izquierda <= derecha:
    medio = (izquierda + derecha) // 2
    if cali_ordenado[medio] == redondeo:
        encontrado = True
        i = calificaciones.index(cali_ordenado[medio])
        print('')
        print("El promedio se encuentra en la pocicion", i+1, "de la lista.")
        break
    elif cali_ordenado[medio] < redondeo:
        izquierda = medio + 1
    else:
        derecha = medio - 1
if not encontrado:
    print('')
    print("El promedio no se encuentra en el arreglo.")
print('')