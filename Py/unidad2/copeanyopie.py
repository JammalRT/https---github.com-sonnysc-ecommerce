import numpy as np

def gauss_jordan(A, b):
  """
  Resuelve un sistema de ecuaciones lineales Ax = b utilizando el método de Gauss-Jordan.

  Args:
    A: La matriz de coeficientes.
    b: El vector de términos independientes.

  Returns:
    El vector de soluciones x.
  """

  n = A.shape[0]

  # Eliminación hacia adelante

  for i in range(n-1):
    for j in range(i+1, n):
      if A[j,i] != 0:
        c = A[j,i] / A[i,i]
        A[j] = A[j] - c * A[i]
        b[j] = b[j] - c * b[i]

  # Eliminación hacia atrás

  x = np.zeros(n)
  x[n-1] = b[n-1] / A[n-1,n-1]
  for i in range(n-2,-1,-1):
    x[i] = (b[i] - np.dot(A[i,i+1:], x[i+1:])) / A[i,i]

  return x

def main():
  # Definimos la matriz de coeficientes

  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

  # Definimos el vector de términos independientes

  b = np.array([1, 2, 3])

  # Resolvemos el sistema de ecuaciones

  x = gauss_jordan(A, b)

  # Imprimimos las soluciones

  print(x)

if __name__ == "__main__":
  main()