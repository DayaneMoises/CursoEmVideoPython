peso = float(input('Informe o peso (Kg): '))
altura = float(input('Informe altura (M): '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Normal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('ATENÇÃO!N\nObesidade móbida!')