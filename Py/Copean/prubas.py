solicitar = 'si'
while solicitar == 'si':
    print('')
    print('====================================================================================================')
    print('')
    print('P Q R')
    print('')
    for P in range(2):
        for Q in range(2):
            for R in range(2):
                print(P,Q,R)
    print('')             
    p = input('=== ')
    opc1 = input('=== ')
    q = input('=== ')
    opc2 = input('=== ')
    r = input('=== ')
    print('')
    if p == '-p':
        P = False
    else:
        P = P 
    if q == '-q':
        Q = False
    else:
        Q = Q
    if r == '-r':
        R = False
    else:
        R = R
    if opc1 == '^':
        for P in range(2):
            for Q in range(2):
                for R in range(2):
                    print(P,Q,R,'\t',int((P and Q)))
        print('')
    elif opc1 == 'v':
        for P in range(2):
            for Q in range(2):
                for R in range(2):
                    print(P,Q,R,'\t',int(((P) or Q)))
        print('')
    elif opc1 == '->':
        for P in range(2):
            for Q in range(2):
                for R in range(2):
                    print(P,Q,R,'\t',int((not((P)) or Q)))
        print('')
    elif opc1 == '<->':
        for p in range(2):
            for q in range(2):
                for r in range(2):
                    print(P,Q,R,'\t',int((((P) and Q) or (not(not P)) and (not Q))))
        print('')
    if opc2 == '^':
        for P in range(2):
            for Q in range(2):
                for R in range(2):
                    print(P,Q,R,'\t',int((P and Q)),'\t',int(P and Q and R))
        print('')
    elif opc2 == 'v':
        for P in range(2):
            for Q in range(2):
                for R in range(2):
                    print(P,Q,R,'\t',int(((P) or Q)),'\t',int(((P) or Q or R)))
        print('')
    elif opc2 == '->':
        for P in range(2):
            for Q in range(2):
                for R in range(2):
                    print(P,Q,R,'\t',int((not((P)) or Q)),'\t',int((not(((((P) and Q))) and (not R)))))
        print('')
    elif opc2 == '<->':
        for P in range(2):
            for Q in range(2):
                for R in range(2):
                    print(P,Q,R,'\t',int((((P) and Q) or (not(not P)) and (not Q))),'\t',int((not((P) and (Q)) and (not(R)) or ((P) and (Q) and (R)))))
        print('')