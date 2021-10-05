n = 50

for i in range(1, n):
    if i == 1:
        aux = 1
        att = 1
        print(f'0 ', end='')
    elif i == 2:
        at = 1
        at = 2
        print(f'1 ', end='')
    else:
        aux = at
        at = at + att
        att = aux
        print(f'{at} ', end='')

