num = int(input('Digite um número inteiro: '))
print('''Bases para conversão
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
conversão = int(input('Informe sua opção: '))
if conversão == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(conversão, bin(num)[2:]))
elif conversão == 2:
    print('{} convertido para OCTAL é igual a {}'.format(conversão, oct(num)[2:]))
elif conversão == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(conversão, hex(num)[2:]))
else:
    print('\nOPÇÃO INVÁLIDA!\nTente novamente.')