import os
os.system('cls')

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Informe a operação (+, -, * ou /): ").strip()

match operador:
    case "+":
        resultado = num1 + num2
        print(f"\nResultado: {num1} {operador} {num2} = {resultado}")
    case "-":
        resultado = num1 - num2
        print(f"\nResultado: {num1} {operador} {num2} = {resultado}")
    case "*":
        resultado = num1 * num2
        print(f"\nResultado: {num1} {operador} {num2} = {resultado}")
    case "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"\nResultado: {num1} {operador} {num2} = {resultado}")
        else:
            print("\nErro: Divisão por zero não é permitida!")
    case _:
        print(f"\nErro: O operador '{operador}' é inválido! Digite +, -, * ou /.")

print('\nFeito por: Camilla')