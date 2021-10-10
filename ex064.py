quantN = 0
quantVx = 0
n = int(input('Digite um número [Para PARAR 999]: '))
while n != 999:
    quantN += 1
    quantVx += n
    n = int(input('Digite um número [Para PARAR 999]: ')) #Foi colocado depois dos dois "contadores" para desconsiderar o 999 como número
print('Você digitou {} números e a soma entre eles foi de {}.'.format(quantN, quantVx))
