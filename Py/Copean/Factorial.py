def factorial(n):
    f = 1
    if n > 0:
        while n > 0:
            f = f*n 
            n = n-1
        return f
    
def permutacion(n,m):
    faca = int(factorial(n))
    facb = int(factorial(n-m))
    return faca/facb

def combinacion(n,m):
    facc = int(factorial(n))
    facd = int(factorial(n-m))
    facm = int(factorial(m))
    res = (facm*facd)
    return (facc/res)
    
sol = 'si'
while sol == 'si':
    print('===================================================================')
    print('')
    print('Quieres hacer:')
    print('')
    print('p = permutacion')
    print('c = combinacion')
    print('f = factorial')
    print('')
    preg = input('===== ')
    print('')
    if preg == 'c':
        print('Combinacion')
        print('')
        n = int(input('ingresa el primer valor: '))
        print('')
        m = int(input('ingresa el segundo valor: '))
        print('')
        print ('la respuesta es',combinacion(n,m))
        print('')   
    elif preg == 'p':
        print('Permutacion')
        print('')
        n = int(input('ingresa el primer valor: '))
        print('')
        m = int(input('ingresa el segundo valor: '))
        print('')
        print('la respuesta es',permutacion(n,m))
        print('')
    elif preg == 'f':
        print('factorial')
        print('')
        n = int(input('ingresa el valor: '))
        print('')
        print ('la respuesta es',factorial(n))
        print('')  