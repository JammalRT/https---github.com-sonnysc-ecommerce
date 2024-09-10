#importamos la libreria 
import numpy as np 
#declaramos los terminos con variable 
A = np.array([[1,1,1],[3,-2,-1],[-2,1,2]])
#declaramos los terminos con terminos independientes 
B = np.array([[2],[4],[2]])
#declaramos una variable para que los valores se aproximen a cero
casicero = 1e-15
#declaramos el tipo de operaciones que queremos hacer que son con punto decimal ya que python no nos da fracciones
A = np.array(A,dtype=float)
#concatenamos las dos matrices con las variables y con los terminos independientes
AB =np.concatenate((A,B),axis=1)
#el copy es para que se guarde la matriz y no se nos cambie 
AB0=np.copy(AB)
#es a donde queremos llegar, a la matriz se conviertan en 0 y 1
tamano=np.shape(AB)
n=tamano[0]
m=tamano[1]
#hacemos el rango para la matriz como nos debe de quedar para llegar a gauss jordan 
for i in range(0,n-1,1):
  #declaramos una variable concatenada con los valores con variable y con los terminos independientes 
  columna = abs(AB[i:,i])
  #despues lo que vamos a hacer con las columnas que se van a cambiar 
  dondemax =np.argmax(columna)
  #declaramos donde van a estar los ceros en la matriz 
  if (dondemax !=0):
    #otra variable para que se guarde la matriz y no se nos cambie 
    temporal=np.copy(AB[i,:])
    #despues el intercambio de operaciones en las filas 
    AB[i,:]=AB[dondemax+i,:]
    AB[dondemax+i,:]=temporal
#el resultado de esas operaciones
AB1 = np.copy(AB)
#empezamos hacer el metodo de gauss original
#declaramos el rango de la matriz
for i in range(0,n-1,1):
  #la multiplicacion de los valores que vamos a cambiar
  pivote=AB[i,i]
  #le sumamos el mas 1 para que los valores no se queden donde mismo 
  adelante = i +1 
  #los valores por lo que los vamos a multiplicar 
  for k in range(adelante,n,1):
    #lo dividimos entre la fila que vamos a cambiar
    factor = AB[k,i]/pivote
    #despues los restamos 
    AB[k,:]=AB[k,:]-AB[i,:]*factor 
#guardamos la matriz que llevamos y le añadimos el copy para que no se nos cambie
AB2 = np.copy(AB)
#le restamos las columnas que nos van a quedar en un valor aproximado a cero y uno y las filas  
ultfila = n-1
ultcolumna =m-1
#declaramos el rango en la matriz de gauss jordan 
for i in range(ultfila,0-1,-1):
  #despues la multiplicacion de las operaciones que vamos a por cambiar 
  pivote=AB[i,i]
  #le restamos menos uno 
  atras= i-1
  #la multiplicacion por la que vamos a restar o sumar 
  for k in range(atras,0-1,-1):
#declaramos la diagonal que nos va a quedar en uno 
    factor=AB[k,i]/pivote
    AB[k,:]=AB[k,:]-AB[i,:]*factor
  AB[i,:]=AB[i,:]/AB[i,i]
  #guardamos el valor en una variable 
x=np.copy(AB[:,ultcolumna])
#esa variable con punto transpose para que los valores nos salgan en vertical 
x=np.transpose([x])
#imprimimos los valores
print('matriz original:')
print(AB1)
print('Gauss Original')
print(AB2)
print('Gauss Jordan')
print(AB)
print('X=', AB[0,3])
print('Y=', AB[1,3])
print('Z=', AB[2,3])