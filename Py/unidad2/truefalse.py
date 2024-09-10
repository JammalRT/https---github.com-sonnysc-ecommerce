#parte del ray
#val1 = p
#val2 = q
#val3 = r

solicitar = input('¿Desea inicar el programa? s/n: ')
while solicitar == 's':
    log = input(''' ¿Que operador logico desea utilizar?
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
#parte del ray
#parte del Jose
    #si variable log es igual a 1
    if log == '1':
        #tabla de conjuncion
        print ('conjuncion')
        print ('P Q R \t S')
        for P in range(2):
            for Q in range(2):
                for R in range(2): 
                    formula = int(P and Q and R)
                    print (P,Q,R,'\t',formula)
        #preguntar si p es negada
        neg1 = input('p negada s/n: ')
        #si p es negada hacer
        if neg1 == 's':
            #entrada de p, q, r
            val1 = int(input('''valor de p: 
            1..... verdadero
            0..... falso: '''))
            val2 = int(input('''valor de q: 
            1..... verdadero
            0..... falso: '''))
            val3 = int(input('''valor de r: 
            1..... verdadero
            0..... falso: '''))
            #declarar variable para negar p
            neg = not (val1)
            #formula de conjugacion
            res = int(neg and val2 and val3)
            print (neg, val2, val3,'\t',res)
            #si variable res es 1 es verdadera
            if res == 1:
                print ('Es verdadera')
            #si variable res es 0 es falso
            elif res == 0:
                print('Es falso')
        #si p no es negada hacer
        elif neg1 == 'n':
            #preguntar si q es negada
            neg2 = input('q es negada s/n: ')
            #si q es negada hacer
            if neg2 == 's':
                #entrada de p, q, r
                val1 = int(input('''valor de p: 
                1..... verdadero
                0..... falso: '''))
                val2 = int(input('''valor de q: 
                1..... verdadero
                0..... falso: '''))
                val3 = int(input('''valor de r: 
                1..... verdadero
                0..... falso: '''))
                #declarar variable para negar q
                neg = not (val2)
                #formula de conjuncion
                res = int(val1 and neg and val3)
                print (val1, neg, val3,'\t',res)
                #si variable res es 1 es verdadera
                if res == 1:
                    print ('Es verdadera')
                #si variable res es 0 es falsa
                elif res == 0:
                    print('Es falso')
            #si q no es negada hacer
            elif neg2 == 'n':
                #preguntar si r es negada
                neg3 = input('r es negada s/n: ')
                if neg3 == 's':
                    #entrada de p, q, r
                    val1 = int(input('''valor de p: 
                    1..... verdadero
                    0..... falso: '''))
                    val2 = int(input('''valor de q: 
                    1..... verdadero
                    0..... falso: '''))
                    val3 = int(input('''valor de r: 
                    1..... verdadero
                    0..... falso: '''))
                    #variable para negar r
                    neg = not (val3)
                    #formula de conjugacion
                    res = int(val1 and val2 and neg)
                    print (val1, val2, neg,'\t',res)
                    #si variable res es 1 es verdadera
                    if res == 1:
                        print ('Es verdadera')
                    #si variable res es 0 es falso
                    elif res == 0:
                        print('Es falso')
                #si p, q, r no eran negadas entonces 
                else:
                    #entrada de p, q, r
                    val1 = int(input('''valor de p: 
                    1..... verdadero
                    0..... falso: '''))
                    val2 = int(input('''valor de q: 
                    1..... verdadero
                    0..... falso: '''))
                    val3 = int(input('''valor de r: 
                    1..... verdadero
                    0..... falso: '''))
                    #formula de conjuncion
                    res = int(val1 and val2 and val3)
                    print (val1, val2, val3,'\t',res)
                    #si variable res es 1 es verdadero
                    if res == 1:
                        print ('Es verdadera')
                    #si variable res es 0 es falso
                    elif res == 0:
                        print('Es falso')
#parte del Jose
#parte del Jammal
    #si variable log es igaual 2
    elif log == '2':
        #tabla de disyuncion
        print ('disyuncion')
        print ('P Q R \t S')
        for P in range(2):
            for Q in range(2):
                for R in range(2): 
                    formula = int(P or Q or R)
                    print (P,Q,R,'\t',formula)
        #preguntar si p es negada
        neg1 = input('p negada s/n: ')
        #si p es negada hacer
        if neg1 == 's':
            #entrada de p, q, r
            val1 = int(input('''valor de p: 
            1..... verdadero
            0..... falso: '''))
            val2 = int(input('''valor de q: 
            1..... verdadero
            0..... falso: '''))
            val3 = int(input('''valor de r: 
            1..... verdadero
            0..... falso: '''))
            #declarar variable para negar p
            neg = not val1
            #formula de disyuncion
            res = int(neg or val2 or val3)
            print (neg, val2, val3,'\t',res)
            #si variable res es 1 es verdadera
            if res == 1:
                print ('Es verdadera')
            #si variable res es 0 es falso
            elif res == 0:
                print('Es falso')
        #si p no es negada hacer
        elif neg1 == 'n':
            #preguntar si q es negada
            neg2 = input('q es negada s/n: ')
            #si q es negada hacer
            if neg2 == 's':
                #entrada de p, q, r
                val1 = int(input('''valor de p: 
                1..... verdadero
                0..... falso: '''))
                val2 = int(input('''valor de q: 
                1..... verdadero
                0..... falso: '''))
                val3 = int(input('''valor de r: 
                1..... verdadero
                0..... falso: '''))
                #declarar variable para negar q
                neg = not val2
                #formula de disyuncion
                res = int(val1 or neg or val3)
                print (val1, neg, val3,'\t',res)
                #si variable res es 1 es verdadera
                if res == 1:
                    print ('Es verdadera')
                #si variable res es 0 es falsa
                elif res == 0:
                    print('Es falso')
            #si q no es negada hacer
            elif neg2 == 'n':
                #preguntar si r es negada
                neg3 = input('r es negada s/n: ')
                if neg3 == 's':
                    #entrada de p, q, r
                    val1 = int(input('''valor de p: 
                    1..... verdadero
                    0..... falso: '''))
                    val2 = int(input('''valor de q: 
                    1..... verdadero
                    0..... falso: '''))
                    val3 = int(input('''valor de r: 
                    1..... verdadero
                    0..... falso: '''))
                    #variable para negar r
                    neg = not val3
                    #formula de disyuncion
                    res = int(val1 or val2 or neg)
                    print (val1, val2, neg,'\t',res)
                    #si variable res es 1 es verdadera
                    if res == 1:
                        print ('Es verdadera')
                    #si variable res es 0 es falso
                    elif res == 0:
                        print('Es falso')
                #si p, q, r no eran negadas entonces 
                else:
                    #entrada de p, q, r
                    val1 = int(input('''valor de p: 
                    1..... verdadero
                    0..... falso: '''))
                    val2 = int(input('''valor de q: 
                    1..... verdadero
                    0..... falso: '''))
                    val3 = int(input('''valor de r: 
                    1..... verdadero
                    0..... falso: '''))
                    #formula de disyuncion
                    res = int(val1 or val2 or val3)
                    print (val1, val2, val3,'\t',res)
                    #si variable res es 1 es verdadero
                    if res == 1:
                        print ('Es verdadera')
                    #si variable res es 0 es falso
                    elif res == 0:
                        print('Es falso')
#parte del Jammal
#parte del Kevin
    elif log == '3':
        #tabla de condicional
        print ('codicional')
        print ('P Q R \t S')
        for P in range(2):
            for Q in range(2):
                for R in range(2): 
                    formula = int(not P) or int(Q)
                    print (P,Q,R,'\t',formula)
        print ('codicional')
        print ('P Q R \t S')
        for P in range(2):
            for Q in range(2):
                for R in range(2): 
                    res1 = int((not P) or int(Q))and int(not R)
                    print (P,Q,R,'\t',res1)
        #preguntar si p es negada
        neg1 = input('p negada s/n: ')
        #si p es negada hacer
        if neg1 == 's':
            #entrada de p, q, r
            val1 = int(input('''valor de p: 
            1..... verdadero
            0..... falso: '''))
            val2 = int(input('''valor de q: 
            1..... verdadero
            0..... falso: '''))
            val3 = int(input('''valor de r: 
            1..... verdadero
            0..... falso: '''))
            #declarar variable para negar p
            neg = not val1
            #formula de condicional
            res = int((not neg) or int(val2)) and val3
            print (neg, val2, val3,'\t',res)
            #si variable res es 1 es verdadera
            if res == 1:
                print ('Es verdadera')
            #si variable res es 0 es falso
            elif res == 0:
                print('Es falso')
        #si p no es negada hacer
        elif neg1 == 'n':
            #preguntar si q es negada
            neg2 = input('q es negada s/n: ')
            #si q es negada hacer
            if neg2 == 's':
                #entrada de p, q, r
                val1 = int(input('''valor de p: 
                1..... verdadero
                0..... falso: '''))
                val2 = int(input('''valor de q: 
                1..... verdadero
                0..... falso: '''))
                val3 = int(input('''valor de r: 
                1..... verdadero
                0..... falso: '''))
                #declarar variable para negar q
                neg = not val2
                #formula de condicional
                res = int((not val1) or int(neg)) and val3
                print (val1, neg, val3,'\t',res)
                #si variable res es 1 es verdadera
                if res == 1:
                    print ('Es verdadera')
                #si variable res es 0 es falsa
                elif res == 0:
                    print('Es falso')
            #si q no es negada hacer
            elif neg2 == 'n':
                #preguntar si r es negada
                neg3 = input('r es negada s/n: ')
                if neg3 == 's':
                    #entrada de p, q, r
                    val1 = int(input('''valor de p: 
                    1..... verdadero
                    0..... falso: '''))
                    val2 = int(input('''valor de q: 
                    1..... verdadero
                    0..... falso: '''))
                    val3 = int(input('''valor de r: 
                    1..... verdadero
                    0..... falso: '''))
                    #variable para negar r
                    neg = not val3
                    #formula de condicional
                    res = int((not val1) or int(val2)) and neg
                    print (val1, val2, neg,'\t',res)
                    #si variable res es 1 es verdadera
                    if res == 1:
                        print ('Es verdadera')
                    #si variable res es 0 es falso
                    elif res == 0:
                        print('Es falso')
                #si p, q, r no eran negadas entonces 
                else:
                    #entrada de p, q, r
                    val1 = int(input('''valor de p: 
                    1..... verdadero
                    0..... falso: '''))
                    val2 = int(input('''valor de q: 
                    1..... verdadero
                    0..... falso: '''))
                    val3 = int(input('''valor de r: 
                    1..... verdadero
                    0..... falso: '''))
                    #formula de condicional
                    res = int((not val1) or int(val2))and val3
                    print (val1, val2, val3,'\t',res)
                    #si variable res es 1 es verdadero
                    if res == 1:
                        print ('Es verdadera')
                    #si variable res es 0 es falso
                    elif res == 0:
                        print('Es falso')
#parte del Kevin

    elif log == '4':
        #tabla de bicondicional
        print ('bicodicional')
        print ('P Q R \t S')
        for P in range(2):
            for Q in range(2):
                for R in range(2): 
                    formula = int(P and Q) or int((not P) and (not Q))
                    print (P,Q,R,'\t',formula)
        #preguntar si p es negada
        neg1 = input('p negada s/n: ')
        #si p es negada hacer
        if neg1 == 's':
            #entrada de p, q, r
            val1 = int(input('''valor de p: 
            1..... verdadero
            0..... falso: '''))
            val2 = int(input('''valor de q: 
            1..... verdadero
            0..... falso: '''))
            val3 = int(input('''valor de r: 
            1..... verdadero
            0..... falso: '''))
            #declarar variable para negar p
            neg = not val1
            #formula de bicondicional
            res = int(neg and val2) or int((not neg) and (not val2))
            print (neg, val2, val3,'\t',res)
            #si variable res es 1 es verdadera
            if res == 1:
                print ('Es verdadera')
            #si variable res es 0 es falso
            elif res == 0:
                print('Es falso')
        #si p no es negada hacer
        elif neg1 == 'n':
            #preguntar si q es negada
            neg2 = input('q es negada s/n: ')
            #si q es negada hacer
            if neg2 == 's':
                #entrada de p, q, r
                val1 = int(input('''valor de p: 
                1..... verdadero
                0..... falso: '''))
                val2 = int(input('''valor de q: 
                1..... verdadero
                0..... falso: '''))
                val3 = int(input('''valor de r: 
                1..... verdadero
                0..... falso: '''))
                #declarar variable para negar q
                neg = not val2
                #formula de bicondicional
                res = int(val1 and neg) or int((not val1) and (not neg))
                print (val1, neg, val3,'\t',res)
                #si variable res es 1 es verdadera
                if res == 1:
                    print ('Es verdadera')
                #si variable res es 0 es falsa
                elif res == 0:
                    print('Es falso')
            #si q no es negada hacer
            elif neg2 == 'n':
                #preguntar si r es negada
                neg3 = input('r es negada s/n: ')
                if neg3 == 's':
                    #entrada de p, q, r
                    val1 = int(input('''valor de p: 
                    1..... verdadero
                    0..... falso: '''))
                    val2 = int(input('''valor de q: 
                    1..... verdadero
                    0..... falso: '''))
                    val3 = int(input('''valor de r: 
                    1..... verdadero
                    0..... falso: '''))
                    #variable para negar r
                    neg = not val3
                    #formula de bicondicional
                    res = int(val1 and val2) or int((not val1) and (not val2))
                    print (val1, val2, neg,'\t',res)
                    #si variable res es 1 es verdadera
                    if res == 1:
                        print ('Es verdadera')
                    #si variable res es 0 es falso
                    elif res == 0:
                        print('Es falso')
                #si p, q, r no eran negadas entonces 
                else:
                    #entrada de p, q, r
                    val1 = int(input('''valor de p: 
                    1..... verdadero
                    0..... falso: '''))
                    val2 = int(input('''valor de q: 
                    1..... verdadero
                    0..... falso: '''))
                    val3 = int(input('''valor de r: 
                    1..... verdadero
                    0..... falso: '''))
                    #formula de bicondicional
                    res = int(neg and val2) or int((not neg) and (not val2))
                    print (val1, val2, val3,'\t',res)
                    #si variable res es 1 es verdadero
                    if res == 1:
                        print ('Es verdadera')
                    #si variable res es 0 es falso
                    elif res == 0:
                        print('Es falso')
    else:
        print('¿Desea correr de nuevo el programa? s/n: ')