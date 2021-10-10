sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F': # pode usar também 'while sexo not in 'MmFf' enquanto não estiver em
        sexo = str(input('Sexo inválido!\nTente novamente: ')).upper().strip()[0]
print('O sexo informado é {}'.format(sexo))
