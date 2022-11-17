# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair
# Seu programa deverá realizar a operação solicitada em cada caso.
n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))
menu = 0
print('''=== Menu ===
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair''')
while menu != 5:
    menu = int(input('Digite a opção desejada: '))
    if menu == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif menu == 2:
        print(f'{n1} * {n2} = {n1 * n2}')
    elif menu == 3:
        if n1 > n2:
            print(f'{n1} é maior do que {n2}')
        elif n1 < n2:
            print(f'{n2} é maior do que {n1}')
        else:
            print(f'{n1} é igual a {n2}')
    elif menu == 4:
        n1 = int(input('1º valor:'))
        n2 = int(input('2º valor:'))
    else:
        print('Opção inválida!')
print('Programa encerrado!')
