salario = float(input('Informe o salário atual do funcionário: '))
if salario <= 1250:
    aumento = salario * 1.15
    print('Quem ganha R$ {:.2f} passará a ganhar o salario de R$ {:.2f} '.format(salario, aumento))
else:
    aumento = salario * 1.10
    print('Quem ganha R$ {:.2f} passará a ganhar o salario de R$ {:.2f} '.format(salario, aumento))