solicitar = 's'
while solicitar == 's':
    negp = input('¿p es negada? s/n: ')
    if negp == 's':
        log = input(''' ¿Que operador logico desea utilizar?
        1 = conjuncion
        2 = disyuncion
        3 = condicional
        4 = bicondicional
        ''')
        if log == '1':
            #tabla de conjuncion
            print ('conjuncion')
            print ('P Q R \t ¬p^q^r')
            for P in range(2):
                for Q in range(2):
                    for R in range(2): 
                        neg = not P
                        formula = int(neg and Q and R)
                        print (P,Q,R,'\t   ',formula)
        elif log == '2':
            #tabla de disyuncion
            print ('disyunción')
            print ('P Q R \t ¬p(or)q(or)r')
            for P in range(2):
                for Q in range(2):
                    for R in range(2): 
                        neg = not P
                        formula = int(neg or Q or R)
                        print (P,Q,R,'\t      ',formula,)
        elif log == '3':
            #tabla de condicional
            print ('condicional')
            print ('P Q R  ¬p^q  (¬p^q)->r')
            for P in range(2):
                for Q in range(2):
                    for R in range(2): 
                        neg = not P
                        formula = int(neg and Q)
                        formula2 = int(not formula) or int(R)
                        print (P,Q,R,'\t',formula, '\t',formula2)
        elif log == '4':
            #tabla de bicondicional
            print ('bicondicional')
            print ('P Q R  ¬p<->q  (¬p<->q)^r')
            for P in range(2):
                for Q in range(2):
                    for R in range(2): 
                        neg = not P
                        formula = int(P and Q) or int((not P) and int(not Q))
                        formula2 = (int(P and Q)) and R or int(not(R and Q) and (not P)) 
                        print (P,Q,R,'\t',formula, '\t',formula2)
    elif negp == 'n':
        negq = input('¿q es negada? s/n: ')
        if negq =='s':
            log = input(''' ¿Que operador logico desea utilizar?
            1 = conjuncion
            2 = disyuncion
            3 = condicional
            4 = bicondicional
            ''')
            if log == '1':
                #tabla de conjuncion
                print ('conjuncion')
                print ('P Q R \t p^¬q^r')
                for P in range(2):
                    for Q in range(2):
                        for R in range(2): 
                            neg = not Q
                            formula = int(P and neg and R)
                            print (P,Q,R,'\t   ',formula,)
            elif log == '2':
                #tabla de disyuncion
                print ('disyunción')
                print ('P Q R  p(or)¬q(or)r')
                for P in range(2):
                    for Q in range(2):
                        for R in range(2): 
                            neg = not Q
                            formula = int(P or neg or R)
                            print (P,Q,R,'\t   ',formula,)
            elif log == '3':
                #tabla de condicional
                print ('condicional')
                print ('P Q R  p^¬q  (p^¬q)->r')
                for P in range(2):
                    for Q in range(2):
                        for R in range(2):
                            neg = not Q
                            formula = int(P and neg)
                            formula2 = int(not formula) or int(R)
                            print (P,Q,R,'\t',formula, '\t',formula2)
            elif log == '4':
                #tabla de bicondicional
                print ('bicondicional')
                print ('P Q R  p<->¬q  (p<->¬q)^r')
                for P in range(2):
                    for Q in range(2):
                        for R in range(2): 
                            neg = not Q
                            formula = int(P and Q) or int((not P) and int(not Q))
                            formula2 = (int(not P) and int(R and (not Q)) or (int(not(not P)) and int(not(R and (not Q)))))
                            print (P,Q,R,'\t',formula, '\t',formula2)
        elif negq == 'n':
            negr = input('¿r es negada? s/n: ')
            if negr =='s':
                log = input(''' ¿Que operador logico desea utilizar?
                1 = conjuncion
                2 = disyuncion
                3 = condicional
                4 = bicondicional
                ''')
                if log == '1':
                    #tabla de conjuncion
                    print ('conjuncion')
                    print ('P Q R \t p^q^¬r')
                    for P in range(2):
                        for Q in range(2):
                            for R in range(2): 
                                neg = not R
                                formula = int(P and Q and neg)
                                print (P,Q,R,'\t   ',formula,)
                elif log == '2':
                    #tabla de disyuncion
                    print ('disyunción')
                    print ('P Q R  p(or)q(or)¬r')
                    for P in range(2):
                        for Q in range(2):
                            for R in range(2): 
                                neg = not R
                                formula = int(P or Q or neg)
                                print (P,Q,R,'\t   ',formula,)
                elif log == '3':
                    #tabla de condicional
                    print ('condicional')
                    print ('P Q R  p^q  (p^q)->¬r')
                    for P in range(2):
                        for Q in range(2):
                            for R in range(2):
                                neg = not R
                                formula = int(P and Q)
                                formula2 = int(not formula) or int(neg)
                                print (P,Q,R,'\t',formula, '\t',formula2)
                elif log == '4':
                    #tabla de bicondicional
                    print ('bicondicional')
                    print ('P Q R  p<->q  (p<->q)^¬r')
                    for P in range(2):
                        for Q in range(2):
                            for R in range(2): 
                                neg = not R
                                formula = int(P and Q) or int((not P) and int(not Q))
                                formula2 = (int(not P) and int(not R and Q)) or (int(not(not P)) and int(not(not R and Q)))
                                print (P,Q,R,'\t',formula, '\t',formula2)
            elif negr == 'n':
                log = input(''' ¿Que operador logico desea utilizar?
                1 = conjuncion
                2 = disyuncion
                3 = condicional
                4 = bicondicional
                ''')
                if log == '1':
                    #tabla de conjuncion
                    print ('conjuncion')
                    print ('P Q R \t p^q^r')
                    for P in range(2):
                        for Q in range(2):
                            for R in range(2):
                                formula = int(P and Q and R)
                                print (P,Q,R,'\t   ',formula,)
                elif log == '2':
                    #tabla de disyuncion
                    print ('disyunción')
                    print ('P Q R  p(or)q(or)r')
                    for P in range(2):
                        for Q in range(2):
                            for R in range(2): 
                                formula = int(P or Q or R)
                                print (P,Q,R,'\t   ',formula,)
                elif log == '3':
                    #tabla de condicional
                    print ('condicional')
                    print ('P Q R  p^q  (p^q)->r')
                    for P in range(2):
                        for Q in range(2):
                            for R in range(2):
                                formula = int(P and Q)
                                formula2 = int(not formula) or int(R)
                                print (P,Q,R,'\t',formula, '\t',formula2)
                elif log == '4':
                    #tabla de bicondicional
                    print ('bicondicional')
                    print ('P Q R  p<->q  (p<->q)^r')
                    for P in range(2):
                        for Q in range(2):
                            for R in range(2): 
                                formula = int(P and Q) or int((not P) and int(not Q))
                                formula2 = (int(not P) and int(R and Q)) or (int(not(not P)) and int(not(R and Q)))
                                print (P,Q,R,'\t',formula, '\t',formula2)
    solicitar = input('¿Desea correr de nuevo el programa? s/n: ')