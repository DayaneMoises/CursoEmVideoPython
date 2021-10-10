"""nome = str(input('Digite seu nome completo: ')).strip().title()
print('Muito prazer em te conhecer!')
separador = nome.split()
print('Seu primeiro noome é {}'.format(separador[0]))
print('Seu segundo nome é {}'.format(separador[2]))"""

nome = str(input('Digite seu nome completo: ')).strip().title()
print('Muito prazer em te conhecer!')
separador = nome.split()
print('Seu primeiro noome é {}'.format(separador[0]))
print('Seu segundo nome é {}'.format(separador[len(separador)-1]))






