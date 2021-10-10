'''pa = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = pa + (10 - 1) * razao
for n in range(pa, decimo + razao, razao):
    print('{:2}'.format(n), end=' -> ')
print('FIM')'''

pa = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = pa  #Para começar a contar. MOSTRA O TERMO
cont = 1 #Começa com 1 porque quero que mostre do 1 ao 10. VAI CONTAR QUANTOS TERMOS
while cont <= 10:
    print('{:2}'.format(termo), end=' -> ')
    termo += razao  #Vai atualizar o termo com base na razao
    cont += 1
print('FIM')
