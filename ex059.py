from time import sleep
maiorN = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('=-=' * 10)
    print('[ 1 ] Somar.\n[ 2 ] Multiplicar.\n[ 3 ] Maior.\n[ 4 ] Informar novos números.\n[ 5 ] Sair do programa.')
    print('=-=' * 10)
    opcao = int(input('>>>>> Selecione opção: '))
    if opcao == 1:
        print('O resultado de {} + {} é {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('O resultado de {} * {} é {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            resultado = n1
        else:
            resultado = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, resultado))
    elif opcao == 4:
        print('>>>> NOVOS NÚMEROS <<<<')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
        print('>>>Programa finalizado!<<<')
    else:
        print('Opção inválida!\nTente novamente.')
