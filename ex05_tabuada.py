import os
import time
os.system('cls || clear')

print('== TABUADA DE MULTIPLICAÇÃO ==')
número = int(input('Digite um número: '))

for i in range(1, 11):
    resultado = número * i
    print(f'{número} x {i} = {resultado}')
    time.sleep(1)

print('\nFeito por: Maria Clara')
print('R.A.: 026.085188')