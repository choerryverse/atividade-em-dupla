import os
os.system('cls')

# Inicialização de variáveis
total_pagar = 0.0
quantidade_pratos = 0

# Exibição do cardápio
print("=" * 40)
print("     CARDÁPIO - RESTAURANTE SABOR DA TERRA     ")
print("=" * 40)
print("Código | Prato                 | Preço")
print("-" * 40)
print("  1    | Feijoada Completa     | R$ 35,00")
print("  2    | Bife a Milanesa       | R$ 28,00")
print("  3    | Frango Grelhado       | R$ 23,00")
print("  4    | Salada Tropical       | R$ 18,00")
print("  5    | Prato do Dia          | R$ 20,00")
print("=" * 40)

while True:
    codigo = input("\nDigite o código do prato desejado: ")

    match codigo:
        case "1":
            prato = "Feijoada Completa"
            preco = 35.00
        case "2":
            prato = "Bife a Milanesa"
            preco = 28.00
        case "3":
            prato = "Frango Grelhado"
            preco = 23.00
        case "4":
            prato = "Salada Tropical"
            preco = 18.00
        case "5":
            prato = "Prato do Dia"
            preco = 20.00
        case _:
            print("Código inválido! Por favor, escolha uma opção do cardápio.")
            continue

    total_pagar += preco
    quantidade_pratos += 1
    print(f"Adicionado: {prato} - R$ {preco:.2f}")

    resposta = input("Deseja outro prato? (S/N): ").strip().upper()
    if resposta == 'N':
        break

print("\n" + "=" * 40)
print("RESUMO DO PEDIDO")
print(f"Quantidade de pratos: {quantidade_pratos}")
print(f"Total a pagar: R$ {total_pagar:.2f}")
print("=" * 40)

print('\nFeito por: Camilla')