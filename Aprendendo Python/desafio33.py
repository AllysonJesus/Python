a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundovalor: '))
c = int(input('Digite o terceiro valor: '))

if a > b and a > c:
    print('O maior valor é {}'.format(a))
if b > a and b > c:
    print('O maior valor é {}'.format(b))
if c > b and c > a:
    print('O maior valor é {}'.format(c))

if a < b and a < b:
    print('O menor valor é {}'.format(a))
if a < b and a < c:
    print('O menor valor é {}'.format(b))
if c < b and c < a:
    print('O menor valor é {}'.format(c))