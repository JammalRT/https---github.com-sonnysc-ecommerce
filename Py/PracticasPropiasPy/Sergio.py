val1 = input('Eres gay: (s/n)')
if val1 == 's':
    print('Ya sabiamos wey >:D')
while val1 == 'n':
        val2 = input('Seguro? (s/n)')
        if val2 == 's':
            val1 = 'n'
        elif val2 == 'n':
            print('Ya sabiamos que eras gay wey >:D')
            break 