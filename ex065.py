#Usar ex055 e ex064 como exemplo
quantNumeros = quantVezes = maiorValor = menorValor = 0
resposta = 'S'
while resposta == 'S':
    valor = int(input("Digite um número: "))
    resposta = str(input('Deseja continuar? [S/N]: ')).upper()
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Digite apenas S ou N. Deseja continuar? [S/N]: ')).upper()
    quantVezes += 1
    quantNumeros += valor
    if quantVezes == 1:
        maiorValor = menorValor = valor
    else:
        if valor > maiorValor:
            maiorValor = valor
        elif valor < menorValor:
            menorValor = valor
print('Você digitou {} números e a média foi de {:.2f}'.format(quantVezes, quantNumeros/quantVezes))
print('O maior valor foi {} e o menor foi {}'.format(maiorValor, menorValor))
