# Crie um programa que exibe um menu de calculadora na tela. O menu exibido deve ser o seguinte:
# Digite 1 para somar dois valores
# Digite 2 para subtrair dois valores
# Digite 3 para multiplicar dois valores
# Digite 4 para dividir dois valores
# Digite 5 para realizar uma potência entre dois valores
# Digite 6 para realizar uma radiciação entre dois valores
# Digite qualquer outro número para sair
# De acordo com a opção informada pelo usuário, solicite os valores
# necessários para o usuário e imprima na tela o resultado da operação realizada.

opcao = int(input("Digite 1 para somar dois valores\n"
                  "Digite 2 para subtrair dois valores\n"
                  "Digite 3 para multiplicar dois valores\n"
                  "Digite 4 para dividir dois valores\n"
                  "Digite 5 para realizar uma potência entre dois valores\n"
                  "Digite 6 para realizar uma radiciação entre dois valores\n"
                  "Digite qualquer outro número para sair\n"))


valor1 = float(input("digite o primeiro valor:"))
valor2 = float(input("digite o segundo valor:"))

if opcao == 1:
    print("Resultado:", valor1 + valor2)
elif opcao == 2:
    print("Resultado:", valor1 - valor2)
elif opcao == 3:
    print("Resultado:", valor1 * valor2)
elif opcao == 4:
    print("Resultado:", valor1 / valor2)
elif opcao == 5:
    print("Resultado:", valor1 ** valor2)
elif opcao == 6:
    print("Resultado:", valor1 ** (1/valor2))
else:
    print("Você saiu!")
