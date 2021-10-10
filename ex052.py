total = 0
num = int(input('Digite um número: '))
for cont in range(1, num + 1):
    if num % cont == 0: #se for divi
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(cont), end='')
print('\n\033[mO numéro {} tem {} múltiplos!'.format(num, total))
if total == 2:
    print('\033[mEle é \033[1;32mprimo\033[m!'.format(num))
else:
    print('Ele \033[1;31mNÃO\033[m é primo!')
