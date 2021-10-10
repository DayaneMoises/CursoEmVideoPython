frase = str(input('Digite uma frase: ')).strip().upper() #eleminou os espaços e deixou maiusculo
palavras = frase.split() #gerou uma lista
junto = ''.join(palavras) #juntou a lista
inverso = junto[::-1]
"""for letra in range(len(junto) - 1, -1, -1): #Fez a lista ficar inversa
    inverso += junto[letra]"""
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO é um palíndromo!')
