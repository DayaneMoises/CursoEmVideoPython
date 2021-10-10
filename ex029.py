velocidade = float(input('Informe a velocidade atual do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Multado!\nVocê excedeu o limite permitido de 80Km/h\nVocê deve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia!\nDirija com segurança!')
