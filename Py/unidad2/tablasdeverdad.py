solicitar = 'si'
while solicitar == 'si':
  log = input(''' ¿Que operador logico desea utilizar?
  1 = conjuncion
  2 = disyuncion
  3 = negacion
  4 = condicional
  5 = bicondicional
  ''')

  if log == '1':
    print ('conjuncion')
    print ('P Q R \t S')
    for P in range(2):
      for Q in range(2):
        for R in range(2):
          formula = int(P and Q and R)
          print (P,Q,R,'\t',formula)
  if log == '2':
    print ('disyuncion')
    print ('P Q R \t S')
    for P in range(2):
      for Q in range(2):
        for R in range(2):
          formula = (P or Q or R)
          print (P,Q,R,'\t',formula)
  if log == '3':
    print ('Negacion')
    neg = input('''¿Desea negar
    P = p
    Q = q
    R = r
    Conjuncion = c
    Disyunción = d
    Condicional = co
    Bicondicional = b: ''')
    if neg == 'p':
      print ('P Q R \t S')
      for P in range(2):
        for Q in range(2):
          for R in range(2):
            formula = int(not P)
            print (P,Q,R,'\t',formula)
    if neg == 'q':
      print ('P Q R \t S')
      for P in range(2):
        for Q in range(2):
          for R in range(2):
            formula = int(not Q)
            print (P,Q,R,'\t',formula)
    if neg == 'r':
      print ('P Q R \t S')
      for P in range(2):
        for Q in range(2):
          for R in range(2):
            formula = int(not R)
            print (P,Q,R,'\t',formula)
    if neg == 'c':
      print ('P Q R \t S')
      for P in range(2):
        for Q in range(2):
          for R in range(2):
            formula = int(P and Q and R)
            con = int(not (formula))
            print (P,Q,R,'\t', con)
    if neg == 'd':
      print ('P Q R \t S')
      for P in range(2):
        for Q in range(2):
          for R in range(2):
            formula = (P or Q or R)
            con = int(not (formula))
            print (P,Q,R,'\t', con)
    if neg == 'co':
      print ('P Q R \t S')
      for P in range(2):
        for Q in range(2):
          for R in range(2):
            formula = (P ^ Q ^ R)
            con = int(not (formula))
            print (P,Q,R,'\t', con)
    if neg == 'b':
      print ('P Q R \t S')
      for P in range(2):
        for Q in range(2):
          for R in range(2):
            formula = (P ^ Q ^ R)
            con = int(not (formula))
            print (P,Q,R,'\t', con)
  if log == '4':
      print ('P Q R \t S')
      for P in range(2):
        for Q in range(2):
          for R in range(2):
            formula = int(not P) or int(Q)
            print (P,Q,R,'\t', formula)
  if log == '5':
      print ('P Q R \t S')
      for P in range(2):
        for Q in range(2):
          for R in range(2):
            formula = int(P and Q) or int((not P) and (not Q))
            print (P,Q,R,'\t', formula)
  solicitar = input('''¿Desea correr denuevo el programa?si/no: ''')