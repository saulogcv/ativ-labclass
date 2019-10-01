def media_final(a1, p1, a2, p2):
    mf= (a1*2 + p1*4 + a2*3 + p2*3)/12
    print('A1: {}    P1: {}'.format (a1, p1))
    print('A2: {}    P2: {}'.format (a2, p2))
    print('MF: {}'.format(round(mf, 2)))

a1 = float(input('A1: '))
p1 = float(input('P1: '))
a2 = float(input('A2: '))
p2 = float(input('P2: '))

media_final(a1, p1, a2, p2)
