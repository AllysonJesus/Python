n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('seu ultimo nome é: {}'.format(len(nome)-1))