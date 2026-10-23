import os
os.system('cls')

renda_mensal = float(input("Informe a renda mensal do cliente (R$): "))
valor_emprestimo = float(input("Informe o valor do empréstimo solicitado (R$): "))
numero_prestacoes = int(input("Informe o número de prestações: "))

prestacao = valor_emprestimo / numero_prestacoes

limite_emprestimo = renda_mensal * 10
limite_prestacao = renda_mensal * 0.30

print(f"\nValor da prestação mensal: R$ {prestacao:.2f}")

if valor_emprestimo <= limite_emprestimo and prestacao <= limite_prestacao:
    print("Resultado: Empréstimo APROVADO")
else:
    print("Resultado: Empréstimo NEGADO")

print('\nFeito por: Camilla')