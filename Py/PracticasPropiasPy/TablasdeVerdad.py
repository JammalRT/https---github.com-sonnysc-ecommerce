def TablaTriple ():
    print('')
    print ('P Q R')
    print('')
def divisor ():
    print('========================================================================================')
solicitar = 'si'
while solicitar == 'si':
    tablaori = 'si'
    if tablaori == 'si':
        print('')
        divisor()
        TablaTriple()
        for P in range(2):
            for Q in range(2):
                for R in range(2):
                    print(P,Q,R)
        print('')
        print('Problema:')
        print('')
        problema = str(input('=== '))
        if problema == 'p^q^r': 
            TablaTriple()
            for P in range(2):
                for Q in range(2):
                    for R in range(2):
                        print(P,Q,R,'\t  ',int(P and Q),'\t  ',int(P and Q and R))
        elif problema == '-p^q^r':
            TablaTriple()
            for P in range(2):
                for Q in range(2):
                    for R in range(2):
                        print(int(not P),Q,R,'\t  ',int((not P) and Q),'\t   ',int((not P) and Q and R))
        elif problema == 'p^-^|+++r':
            TablaTriple()
            for P in range(2):
                for Q in range(2):
                    for R in range(2):
                        print(int(not P),Q,R,'\t  ',int((not P) and Q),'\t   ',int((not P) and Q and R))
        elif problema == '-p^q^r':
            TablaTriple()
            for P in range(2):
                for Q in range(2):
                    for R in range(2):
                        print(int(not P),Q,R,'\t  ',int((not P) and Q),'\t   ',int((not P) and Q and R))