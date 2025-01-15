# Crie um programa que imprime a tabuada de um número qualquer digitado pelo usuário.

valor = int(input("Digite um valor:"))

for i in range(1, 11):
    tabuada = i * valor
    print(tabuada)
