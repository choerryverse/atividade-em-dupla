import os
os.system('cls || clear')

TENTATIVAS_MAX = 3
senha = None
cadastro = None

print('== CADASTRO DE USUÁRIO ==')
while cadastro is None or senha is None:
    if cadastro is None:
        cadastro = input('Digite um nome de usuário: ')
    if senha is None:
        senha = input('Digite uma senha: ')
    break

os.system('cls || clear')

print('== LOGIN DE USUÁRIO ==')
tentativas = 0
while tentativas < TENTATIVAS_MAX:
    usuario = input('Digite o nome de usuário: ')
    senha_digitada = input('Digite a senha: ')

    if usuario == cadastro and senha_digitada == senha:
        print(f'\nOlá, {cadastro}! Bem vindo!')
        break
    else:
        tentativas += 1
        print(f'\nUsuário ou senha incorretos. Tentativa {tentativas} de {TENTATIVAS_MAX}.\n')
        if tentativas == TENTATIVAS_MAX:
            print('Número máximo de tentativas atingido. Acesso negado.')
            break

print('\nFeito por: Maria Clara')
print('R.A.: 026.085188')