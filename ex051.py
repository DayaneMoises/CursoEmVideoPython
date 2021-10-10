pa = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = pa + (10 - 1) * razao
for n in range(pa, decimo + razao, razao):
    print('{:2}'.format(n), end=' -> ')
print('FIM')
