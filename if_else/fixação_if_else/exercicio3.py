# Crie um programa que recebe dois valores inteiros A e B pelo teclado e imprime o valor de A dividido por B.
# Entretanto, se o valor de B for 0, imprima uma mensagem de erro e não faça a divisão.

a = int(input("Digite um valor do dividendo:"))
b = int(input("Digite um valor do divisor:"))

if b == 0:
    print("Erro!")
else:
    print("O valor da divisão é:", (a / b))
