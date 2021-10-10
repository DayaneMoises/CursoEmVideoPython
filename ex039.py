import datetime
nascimento = int(input('Ano de nascimento: '))
anoAtual = datetime.datetime.now()
idade = anoAtual.year - nascimento
print('Você nasceu em {} e tem {} anos em {}.'.format(nascimento, idade, anoAtual.year))
if idade <= 17:
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(anoAtual.year + (18 - idade)))
elif idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
else:
    diferenca = idade - 18
    anoDeAlistamento = anoAtual.year - diferenca
    print('Para o seu próprio bem, espero que você já tenha se alistado em {}!'.format(anoDeAlistamento))

'''from datetime import date
nascimento = int(input('Ano de nascimento: '))
anoAtual = date.today().year
print('Você nasceu em {} e tem {} anos em {}.'.format(nascimento, (anoAtual - nascimento), anoAtual))
if (anoAtual - nascimento) <= 17:
    anosParaAlistamento = anoAtual- nascimento
    print('Ainda faltam {} anos para o alistamento.'.format(18 - anosParaAlistamento))
    print('Seu alistamento será em {}.'.format(anoAtual + (18 - anosParaAlistamento)))
elif (anoAtual - nascimento) == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
else:
    diferenca = (anoAtual - nascimento) - 18
    alistamento = anoAtual - diferenca
    print('Para o seu próprio bem, espero que você já tenha se alistado em {}!'.format(alistamento))'''