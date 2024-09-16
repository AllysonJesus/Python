d = float(input('O carro foi alugado por quantos dias? '))
km = int(input('Quantos km foram percorridos '))

valor = (d * 60) + (km * 0.15)

print('O carro foi alugado por {} dias, percorreu {} km e será preciso pagar R${:.2f}'.format(d,km,valor))