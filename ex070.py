print('         LOJA TUDO BARATO')
totalC = contPreco = cont = menorPreco = nomePreco = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        nomePreco = produto
    totalC += preco
    if preco >= 1000:
        contPreco += 1
    continuar = str(input('Continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        print('---- FIM DO PROGRAMA ----')
        break
print(f'Total da compra: R$ {totalC:.2f}')
print(f'Total de produtos que custam mais de R$ 1.000,00: {contPreco}')
print(f'Produto mais barato: {nomePreco} no valor de R$ {menorPreco:.2f}')
