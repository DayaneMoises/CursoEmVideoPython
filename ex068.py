from random import randint
c = 0
print('~=~=~=~ Jogo do PAR ou IMPAR =~~=~=~')
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    escolha = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).upper().strip()
    print('=*' * 20)
    resultado = computador + jogador
    if escolha == 'P' and resultado % 2 == 0:
        print('VOCÊ GANHOU!')
        print(f'O resultado foi PAR!')
    elif escolha == 'I' and resultado % 2 == 1:
        print('VOCÊ GANHOU!')
        print(f'O resultado foi IMPAR!')
    else:
        print('VOCÊ PERDEU!')
        break
    c +=1
print(f'Você jogou {jogador} e o computador {computador}. O total foi de {resultado}.')
print(f'No total você venceu {c} vezes!')
