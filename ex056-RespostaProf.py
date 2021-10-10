somaIdade = 0
médiaIdade = 0
maiorIdadeDeHomem = 0
nomeVelho = ''
totalMulher20 = 0
for p in range(1, 5):
    print('=*=*=*=*=* ª{} pessoa *=*=*=*=*='.format(p))
    nome = str(input('Nome: ')).capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F ou M]: '))
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeDeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeDeHomem:
        maiorIdadeDeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher20 += 1
médiaIdade = somaIdade / p
print('A média de idade do grupo é de {} anos'.format(médiaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeDeHomem, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalMulher20))
