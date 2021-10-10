soma = 0
contador = 0
print('Você precisa informar 6 números!')
for n in range(1, 7):
    n = int(input('Digite um números: '))
    if n % 2 == 0:
        soma += n
        contador += 1
print('A soma dos números pares é de {} de um total de {} números PARES informados.'.format(soma, contador))

