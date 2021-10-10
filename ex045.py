from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opçãoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('-=' * 15)
print('O computador escolheu {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print('Jogador GANHOU!')
    elif jogador == 2:
        print('Computador GANHOU!')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print("Computador GANHOU!")
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador GANHOU!')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print("Jogador GANHOU!")
    elif jogador == 1:
        print('Computador GANHOU!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada INVÁLIDA!')
