# Crie um programa que imprime na tela todos os valores entre dois valores digitados pelo teclado.

valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))

lista = range(valor1, valor2)

for i in lista:
    print(i)
