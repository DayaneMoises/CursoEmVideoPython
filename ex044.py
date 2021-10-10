valor = float(input('Preço do produto: R$ '))
print('''FORMAS DE PAGAMENTO:
      [ 1 ] à vista dinheiro' #desconto de 10%
      [ 2 ] à vista cartão' #desconto 5%
      [ 3 ] 2x no cartão' #preço normal
      [ 4 ] 3x ou mais no cartão') #20% de juros''')
opcao = int(input('Informe a forma de pagamento escolhida: '))
if opcao == 1:
    desconto = valor - (valor * 0.10)
    print('Com base na sua compra de R$ {:.2f} o valor a ser pago será de R$ {:.2f} '.format(valor, desconto))
elif opcao == 2:
    desconto = valor - (valor * 0.05)
    print('Com base na sua compra de R$ {:.2f} o valor a ser pago será de R$ {:.2f} '.format(valor, desconto))
elif opcao == 3:
    parcela = valor / 2
    print('Com base na sua compra de R$ {:.2f} valor a ser pago será 2x de  R$ {:.2f} '.format(valor, parcela))
elif opcao == 4:
    juros = valor * 1.20
    Qparcela = int(input('Quantas parcelas: '))
    parcela = juros / Qparcela
    print('''Valor original da compra R$ {:.2f} 
    Valor com o acrescimo do juros R$ {:.2f}
    Valor das {}x parcelas a serem pagas R$ {:.2f}''' .format(valor, juros, Qparcela, parcela))
else:
    print('Opção invalida, tente novamente!')
