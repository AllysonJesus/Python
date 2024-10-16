v = float(input('Qual a velocidade atual? '))
if v > 80:
    multa = (v - 80) * 7
    print('Você excedeu o limite de velocidade e recebeu uma multa de {}'.format(multa))
else:
    print('Você está no limite de velocidade permitido')    