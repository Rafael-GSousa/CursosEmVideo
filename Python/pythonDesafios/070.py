# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra;
# B) Quantos produtos custam mais de R$1000;
# C) Qual é o nome do produto mais barato.
print('-' * 30)
print(f'{"LOJA SUPER BARATÃO":^30}')
print('-' * 30)
total = contMil = baratoPreco = contProduto = 0
baratoNome = ''
while True:
    produto = str(input('Nome do Produto: ')).strip().capitalize()
    preco = float(input('Preço do Produto: R$'))
    if preco > 1000:
        contMil += 1
    total += preco
    contProduto += 1
    if contProduto == 1:
        baratoNome = produto
        baratoPreco = preco
    elif baratoPreco > preco:
        baratoPreco = preco
        baratoNome = produto
    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continua in 'N':
        break
    else:
        while continua != 'S':
            continua = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
print(f'{" FIM DO PROGRAMA ":-^30}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {contMil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {baratoNome} que custa R${baratoPreco:.2f}')
