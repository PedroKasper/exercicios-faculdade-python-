# Crie um programa que recebe um inteiro pelo teclado e imprime se ele é par ou ímpar.

a = int(input("Digite um número:"))

if a != 0 and a % 2 == 0:
    print("O número digitado é par")
else:
    print("O número é ímpar")
