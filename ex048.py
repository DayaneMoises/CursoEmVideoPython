soma = 0
contador = 0
contador1 = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        contador += 1
        soma += n
    contador1 += 1
print('Temos um total de {} números, mas apenas {} são múltiplos de três!'.format(contador1, contador))
print('A SOMA de TODOS os {} valores solicitados é de {}'.format(contador, soma))

#n % 3 == 0 saber se é divisivel por 3