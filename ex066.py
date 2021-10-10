soma = quantVx = 0
while True:
    numero = int(input('Digite um valor [Para parar: 999]: '))
    if numero == 999:
        break
    soma += numero
    quantVx += 1
print(f'Soma dos {quantVx} valores foi de {soma}')
