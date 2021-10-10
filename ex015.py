km = float(input('Qual a quantidade de KM percorridos: '))
dias = float(input('Por quantos dias ele foi alugado: '))
totalApagar = (km * 0.15) + (dias * 60)
print('Com base no total de {} KM percorridos e de {} dias em uso, o valor a ser pago será de {}'.format(km, dias, totalApagar))
