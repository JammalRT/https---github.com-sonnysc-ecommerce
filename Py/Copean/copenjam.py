#El equipo esta comformado por:
#-Jammal Rodrigues
#-Kevin Valencia 
#-Sergio Soto
#-Jose Rodrigues 
#-Raymundo Renteria 
solicitar = 'si'
while solicitar == 'si':
    tablaori = 'si'
    if tablaori == 'si':
            print('')
            print ('P Q R')
            print('')
            for P in range(2):
                for Q in range(2):
                    for R in range(2):
                        print (P,Q,R)
                                             
            negp = input('p es negada? (si/no) ')
            if negp == 'si':
                resl = ('¬P')
                print('')
                print ('P Q R\t¬P')
                print('')
                for P in range(2):
                    for Q in range(2):
                        for R in range(2):
                            print (P,Q,R,'\t',int(not P))
                            
                opclog = input(''' Operador logico:
    1 = conjuncion
    2 = disyuncion
    3 = condicional        
    4 = bicondicional
    ''')
                if opclog == '1':
                    print(resl,'conjuncion con:')
                    negq = input('q es negada? (si/no) ')
                    if negq == 'si':
                        print('')
                        print ('P Q R\t¬P ^ ¬Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    print (int(not P),int(not Q),R,'\t  ',int(not P) and int(not Q)) 
                                     
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^¬Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t  ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^¬Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t  ',formula2)

                            if opclog2 == '3':
                                print('¬P^¬Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t->¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and not (R)))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t  ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^¬Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t  ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('')     
                                               
                    elif negq == 'no':
                        print('P Q R\t',resl,'^ Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    formula = int((not P) and Q)
                                    print(int(not P),Q,R,'\t  ',formula)
                                    
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int((not P) and  Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),Q,int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int((not P) and  Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),Q,R,'\t  ',formula,'\t  ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int((not P) and Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),Q,int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int((not P) and  Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),Q,R,'\t  ',formula,'\t   ',formula2)

                            if opclog2 == '3':
                                print('¬P^Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^Q)\t -> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int((not P) and  Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),Q,int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int((not P) and  Q)
                                                formula2 = int(not(((P and (not Q))) and not (R)))
                                                print(int(not P),Q,R,'\t  ',formula,'\t  ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int((not P) and  Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),Q,int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int((not P) and  Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),Q,R,'\t  ',formula,'\t  ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('') 
                elif opclog == '2':
                    print(resl,'disyucion con:')
                    negq = input('q es negada? (si/no) ')
                    if negq == 'si':
                        print('')
                        print ('P Q R\t¬P v ¬Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    print (int(not P),int(not Q),R,'\t  ',int(not P) or int(not Q))
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^¬Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t    ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t    ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^¬Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t    ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t    ',formula2)

                            if opclog2 == '3':
                                print('¬P^¬Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t->¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and not (R)))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t    ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^¬Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t    ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('')
                    elif negq == 'no':
                        print('P Q R\t',resl,'v Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    formula = int((not P) or Q)
                                    print(int(not P),Q,R,'\t  ',formula)
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^¬Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t  ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^¬Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t  ',formula2)

                            if opclog2 == '3':
                                print('¬P^¬Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t->¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and not (R)))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t  ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^¬Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('')
                                        
                elif opclog == '3':
                    print(resl,'condicional con:')
                    negq = input('q es negada? (si/no) ')
                    if negq == 'si':
                        print('')
                        print ('P Q R\t¬P -> ¬Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    print (int(not P),int(not Q),R,'\t  ',int(not(not P) or int(not Q))) 
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^¬Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t  ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^¬Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t  ',formula2)

                            if opclog2 == '3':
                                print('¬P^¬Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t->¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and not (R)))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t  ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^¬Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t  ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('')       
                                  
                    elif negq == 'no':
                        print('P Q R\t',resl,'-> Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    formula = int(not(not P) or Q)
                                    print(int(not P),Q,R,'\t  ',formula)
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^¬Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^¬Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t  ',formula2)

                            if opclog2 == '3':
                                print('¬P^¬Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t->¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and not (R)))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^¬Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('')
                            
                elif opclog == '4':
                    print(resl,'bicondicional con:')
                    negq = input('q es negada? (si/no) ')
                    if negq == 'si':
                        print('')
                        print ('P Q R\t¬P <-> ¬Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    print (int(not P),int(not Q),R,'\t  ',int(P and Q) or int((not P) and int(not Q)))
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^¬Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^¬Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)

                            if opclog2 == '3':
                                print('¬P^¬Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t->¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and not (R)))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^¬Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('')
                            
                    elif negq == 'no':
                        print('P Q R\t',resl,'<-> Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    formula = int((not P) and Q) or int(not(not P) and (not Q))
                                    print(int(not P),Q,R,'\t  ',formula)
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^¬Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^¬Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)

                            if opclog2 == '3':
                                print('¬P^¬Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t->¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and not (R)))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^¬Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('')
                            
            elif negp == 'no':
                resl = ('P')            
                print('')
                opclog = input(''' Operador logico:
    1 = conjuncion
    2 = disyuncion
    3 = condicional        
    4 = bicondicional
    ''')
                if opclog == '1':
                    print(resl,'conjuncion con:')
                    negq = input('q es negada? (si/no) ')
                    if negq == 'si':
                        print('')
                        print ('P Q R\t',resl,'^ ¬Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    formula = int(P and int(not Q))
                                    print(P,(int(not Q)),R,'\t  ',formula)  
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^¬Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^¬Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)

                            if opclog2 == '3':
                                print('¬P^¬Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t->¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and not (R)))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^¬Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('')
                                           
                    elif negq == 'no':
                        print('')
                        print ('P Q R\t',resl,'^ Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    formula = int(P and Q)
                                    print(P,Q,R,'\t  ',formula)
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^¬Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^¬Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)

                            if opclog2 == '3':
                                print('¬P^¬Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t->¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and not (R)))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^¬Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('')
                            
                elif opclog == '2':
                    print(resl,'disyucion con:')
                    negq = input('q es negada? (si/no) ')
                    if negq == 'si':
                        print('')
                        print ('P Q R\t P v ¬Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    print (P,int(not Q),R,'\t  ',int(P or int(not Q))) 
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^¬Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^¬Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)

                            if opclog2 == '3':
                                print('¬P^¬Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t->¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and not (R)))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^¬Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('')
                             
                    elif negq == 'no':
                        print('P Q R\t',resl,'v Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    formula = int(P or Q)
                                    print(P,Q,R,'\t  ',formula)
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^¬Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^¬Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)

                            if opclog2 == '3':
                                print('¬P^¬Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t->¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and not (R)))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t    ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^¬Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t    ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('')
                            
                elif opclog == '3':
                    print(resl,'condicional con:')
                    negq = input('q es negada? (si/no) ')
                    if negq == 'si':
                        print('')
                        print ('P Q R\tP -> ¬Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    print (P,int(not Q),R,'\t  ',int(not P) or int(not Q)) 
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^¬Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^¬Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)

                            if opclog2 == '3':
                                print('¬P^¬Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t->¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and not (R)))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t    ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^¬Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('')
                            
                    elif negq == 'no':
                        print('P Q R\t',resl,'-> Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    formula = int((not P) or Q)
                                    print(P,Q,R,'\t  ',formula)
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^¬Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^¬Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)

                            if opclog2 == '3':
                                print('¬P^¬Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t->¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and not (R)))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^¬Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('')
                            
                elif opclog == '4':
                    print(resl,'bicondicional con:')
                    negq = input('q es negada? (si/no) ')
                    if negq == 'si':
                        print('')
                        print ('P Q R\tP <-> ¬Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    print (P,int(not Q),R,'\t  ',int((not P) and Q) or int(not(not P) and (not Q)))
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^¬Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^¬Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)

                            if opclog2 == '3':
                                print('¬P^¬Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t->¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t  ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and not (R)))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^¬Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t    ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('')
                            
                    elif negq == 'no':
                        print('P Q R\t',resl,'<-> Q')
                        print('')
                        for P in range(2):
                            for Q in range(2):
                                for R in range(2):
                                    formula = int(P and Q) or ((not P) and (not Q))
                                    print(P,Q,R,'\t  ',formula)
                        agrer = input('Agregar r? (si/no) ')
                        if agrer == 'si':
                            opclog2 = input('''operacion logica:
    1 = conjuncion
    2 = disyuncion
    3 = condicional
    4 = bicondicional
    ''')
                            if opclog2 == '1':
                                print('¬P^¬Q conjuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t ^ ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and (not R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t    ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t ^ R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P and (not Q) and R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t    ',formula2)
                                                
                            if opclog2 == '2':
                                print('¬P^¬Q disyuncion con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t v ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not P) or int(not Q) or int(not R)
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t v R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int((not P) or int(not Q) or R)
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)

                            if opclog2 == '3':
                                print('¬P^¬Q condicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q^)\t->¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and R))
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t -> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((((not P) and (not Q))) and not (R)))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t   ',formula2)
                                                
                            if opclog2 == '4':
                                print('¬P^¬Q bicondicional con:')
                                negr = input('r es negada? (si/no) ')
                                if negr == 'si':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> ¬R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not(not R))) or int(((not P) and (not Q) and (not R))) 
                                                print(int(not P),int(not Q),int(not R),'\t  ',formula,'\t   ',formula2)
                                elif negr == 'no':
                                    print('')
                                    print ('P Q R\t(¬P^¬Q)\t <-> R')
                                    print('')
                                    for P in range(2):
                                        for Q in range(2):
                                            for R in range(2):
                                                formula = int(not P) and int(not Q)
                                                formula2 = int(not((not P) and (not Q)) and (not R)) or int(((not P) and (not Q) and R))
                                                print(int(not P),int(not Q),R,'\t  ',formula,'\t  ',formula2)
                                                
                        elif agrer == 'no':
                            print('')
                            print('-------------------------------------')
                            print('')