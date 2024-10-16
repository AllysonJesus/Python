sal = float(input('Digite seu salário: R$'))

if sal <= 1250:
    aumento = sal +(sal * (15/100))
    print('O seu salario teve um aumento de 15% e é {} '.format(aumento))
else:
    aumento = sal + (sal * (10 / 100))
    print('O seu salario com um aumento de 10% e é {} '.format(aumento))