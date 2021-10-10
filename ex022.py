nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Se nome em letras maiúsculas é {}'.format(nome.upper()))
print('Se nome em letras minúsculas é {}'.format(nome.lower()))
print('Se nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
separando = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separando[0], len(separando[0])))




