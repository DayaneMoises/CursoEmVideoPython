from random import randint
computador = randint(0, 10)
jogador = int(input('Digite um número de 1 a 10: '))
palpites = 0
while computador != jogador:
    print('Você ERROU!')
    if computador > jogador:
        print('Tente um número MAIOR!')
    else:
        print('Tente um número MENOR!')
    jogador = int(input('Tente novamente: '))
    palpites += 1
print('Você precisou de {} tentativas para acertar!'.format(palpites))
