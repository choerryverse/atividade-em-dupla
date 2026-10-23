import os
os.system('cls || clear')

QUANTIDADE = 5
pares = 0
impares = 0
soma_numeros = 0

print('== PARES E IMPARES ==')

for i in range(QUANTIDADE):
    numero = int(input(f"Digite o {i + 1}º número: "))
    soma_numeros += numero
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1


print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Soma dos números digitados: {soma_numeros}")

print('\nFeito por: Maria Clara')
print('R.A.: 026.085188')