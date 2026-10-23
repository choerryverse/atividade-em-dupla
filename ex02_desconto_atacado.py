import os
os.system('cls || clear')

print('== DESCONTO ATACADO ==')
nome_produto = input('Digite o nome do produto: ')
preco_produto = float(input('Digite o preço unitário do produto: R$ '))
quantidade = int(input('Digite a quantidade de produtos: '))

total = preco_produto * quantidade

if quantidade >= 5:
    desconto = total * 0.02
elif quantidade >= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

preco_final = total - desconto

print(f'Produto: {nome_produto}')
print(f'Total: R$ {total:.2f}')
print(f'Desconto: R$ {desconto:.2f}')
print(f'Preço final: R$ {preco_final:.2f}')

print('\nFeito por: Maria Clara')
print('R.A.: 026.085188')