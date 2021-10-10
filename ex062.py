pa = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = pa
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais #Total a ser mostrato é total (que é zero) + mais (quantos termos a maior ele quer)
    while cont <= total:    #total de termos
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Informe quantos termos você quer mosntrar a mais [Para concluir digite 0]: '))
print('Progressão finalizada com {} termos mostrados.'.format(total))