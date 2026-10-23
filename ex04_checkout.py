import os
os.system('cls')

valor_produto = float(input("Informe o valor do produto (R$): "))
forma_pagamento = int(input("Forma de pagamento (1 para À vista, 2 para A prazo): "))

if forma_pagamento == 1:
    desconto = valor_produto * 0.10
    valor_total = valor_produto - desconto
    
    print("\n--- RESUMO DO CHECKOUT ---")
    print(f"Valor original: R$ {valor_produto:.2f}")
    print("Forma de pagamento: À vista")
    print(f"Desconto (10%): R$ {desconto:.2f}")
    print(f"Valor total a pagar: R$ {valor_total:.2f}")

elif forma_pagamento == 2:
    parcelas = int(input("Informe a quantidade de parcelas (no máximo 6): "))
    
    if 1 <= parcelas <= 6:
        valor_parcela = valor_produto / parcelas
        
        print("\n--- RESUMO DO CHECKOUT ---")
        print(f"Valor original: R$ {valor_produto:.2f}")
        print("Forma de pagamento: A prazo")
        print(f"Quantidade de parcelas: {parcelas}x")
        print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
        print(f"Valor total a pagar: R$ {valor_produto:.2f}")
    else:
        print("\nErro: O número de parcelas deve ser de 1 a 6.")

else:
    print("\nErro: Forma de pagamento inválida. Digite 1 para à vista ou 2 para a prazo.")