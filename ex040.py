n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Com base nas notas {:.1f} e {:.1f} a média será de {:.1f}'.format(n1, n2, media))
if media <=4:
    print('O aluno está REPROVADO!')
elif media >= 5 and media < 7:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno está APROVADO!')
