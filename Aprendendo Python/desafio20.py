from random import shuffle

a1 = str(input('Qual o nome do primeiro aluno(a)? '))
a2 = str(input('Qual o nome do segundo aluno(a)? '))
a3 = str(input('Qual o nome do terceiro aluno(a)? '))
a4 = str(input('Qual o nome do quarto aluno(a)? '))

alunos = [a1,a2,a3,a4]
shuffle(alunos)

print('A ordem de apresentação será: ')
print(alunos)