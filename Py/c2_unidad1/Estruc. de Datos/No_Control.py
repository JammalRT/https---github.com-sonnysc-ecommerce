edades = [18,20,24,19,18,25,26,20,22,23]
No_control = [18040245,57265741,98452526,54983615,22654587,32458967,32142565,54697825,65742416,21362471]
print('Este es el rango de 4to al 8vo:',No_control[4:8])
print('El de la 9na pocision es:',No_control[9])
edades.sort(reverse=True)
print('El alumno con mayor edad es:',edades[0],'Y su numero de control es:',No_control[6])