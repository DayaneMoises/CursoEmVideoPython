vlCasa = float(input('Informe valor da casa R$ '))
salario = float(input('Informe salário mensal R$ '))
anos = int(input('Informe quantos anos deseja financiar: '))
prestaçao = vlCasa / (anos * 12)
maxPrestaçao = salario * 0.30

if prestaçao >= maxPrestaçao:
    print('Empréstimo NEGADO! \nInfelizmente o valor da prestação excede o limite de 30% do seu salário')
else:
    print('Empréstimo CONCEDIDO!')

print('Com base em uma casa no valor de R$ {:.2f} com financiamento de {} '.format(vlCasa, anos), end='')
print(' a prestação será de R$ {:.2f}'.format(prestaçao))
