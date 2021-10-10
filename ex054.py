from datetime import date
ano = date.today().year
contMaior = 0
contMenor = 0
for pessoa in range(1, 8):
    nascimento = int(input('Informe o ano que a {}ª pessoa nascimento: '.format(pessoa)))
    idade = ano - nascimento
    if idade >= 21:
        contMaior += 1
    else:
        contMenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(contMaior))
print('E também tivemos {} pessoas menores de idade'.format(contMenor))