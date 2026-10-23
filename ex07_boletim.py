import os
os.system('cls')

soma_notas = 0

for i in range(1, 4):
    while True:
        nota = float(input(f"Digite a {i}ª nota (entre 0 e 10): "))
        
        if 0 <= nota <= 10:
            soma_notas += nota
            break
        else:
            print("Nota inválida! Por favor, digite um valor entre 0 e 10.")

media = soma_notas / 3

print(f"\nMédia do aluno: {media:.2f}")

if media >= 7:
    print("Situação: Aprovado")
elif 5 <= media <= 6.9:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")

print('\nFeito por: Camilla')