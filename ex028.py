from random import randrange
from time import sleep

print('Vou pensar em um número entre 0 e 5. Será que você consegue adivinhar qual?')
num = int(input('Digite o número que eu pensei: '))
surpresa = randrange(5)
print('Procesando... ')
sleep(2)

if num == surpresa:
    print('Parabens! \nO número que você escolheu é o {} e eu pensei no {}!'.format(num, surpresa))
else:
    print('Parece que você não é tão bom assim, não é mesmo? \nO número que você escolheu é o {} e eu pensei no {}!'.format(num, surpresa))
