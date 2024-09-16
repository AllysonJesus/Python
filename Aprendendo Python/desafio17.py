import math
op = float(input('Cateto oposto: '))
ad = float(input('Cateto adjacente: '))

hip = math.hypot(op,ad)

print('A hipotenusa será: {:.2f}'.format(hip))