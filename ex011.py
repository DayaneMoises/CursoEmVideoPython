largura = float(input('Informe o largura da parede em metros: '))
altura = float(input('Informe a altura da parede em metros: '))
mQradrados = altura * largura
tinta = mQradrados / 2

print('Com base em {} m² de parede, será necessario {} litros de tinta para pintar toda a parede.'.format(mQradrados, tinta))