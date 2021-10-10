from time import sleep

km = float(input('Informe a distância da sua viagem em Km: '))
print('Sua viagem será de {}Km. Com base nisso iremos processar o valor a ser pago.'.format(km))
print('Processando...\n')
sleep(2)

'''if km <= 200:
    preco = km * 0.50
    print('O preço da sua passagem será de R$ {:.2f}'.format(preco))
else:
    preco = km * 0.45
    print('O preço da sua passagem será de R$ {:.2f}'.format(preco))'''

preco = km * 0.50 if km <= 200 else km * 0.45 #simplificado 
print('O preço da sua passagem será de R$ {:.2f}'.format(preco))
