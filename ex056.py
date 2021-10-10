somaIdade = 0
mediaIdade = 0
maisVelho = 0
fMaior = 0
nomeVelho = ''
for cont in range(1, 5):
    nome = str(input('Nome da ª{} pessoa: '.format(cont))).capitalize()
    idade = int(input('Idade: '))
    if idade:
        somaIdade += idade
        mediaIdade = somaIdade / cont
    sexo = str(input('Sexo (F ou M): ')).upper()
    if cont == 1 and sexo == 'M':
        maisVelho = idade
        nomeVelho = nome
    if sexo == 'M' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome
    if sexo == 'F' and idade <= 19:
        fMaior += 1
print('A média de idade do grupo é de {}.'.format(mediaIdade))
print('O nome do HOMEM mais velho é {}.'.format(nomeVelho))
print('Total de mulheres com MENOS de 20 anos é de {} pessoa.'.format(fMaior))
