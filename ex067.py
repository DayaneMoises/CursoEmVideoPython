while True:
    tabuada = int(input('Informe qual tabuada deseja ver: '))
    if tabuada <= -1:
        break
    print('=*'*17)
    for n in range(1, 11):
        print(f'{tabuada:2} x {n:2} = {n*tabuada:2}')
    print('=*' * 17)
