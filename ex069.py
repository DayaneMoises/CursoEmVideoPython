print('CADASTRO DE PESSOAS')
contadorIdade = contadorM = contadorF = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        contadorIdade += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        contadorM += 1
    elif sexo == 'F' and idade < 20:
        contadorF += 1
    continuar = str(input('Continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        print('Cadastro finalizado!')
        break
print('=*'*22)
print(f'Total de pessoas com mais de 18 anos: {contadorIdade}')
print(f'Total de homens cadastratos: {contadorM}')
print(f'Total de mulheres com menos de 20 anos: {contadorF}')
print('=*'*22)
