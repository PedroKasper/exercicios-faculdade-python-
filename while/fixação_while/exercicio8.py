# Crie um programa que pergunta para o usuário (via Teclado) quantos números ele irá digitar
# e armazena em uma variável chamada quant. Logo após, faça com que o usuário digite quant números inteiros,
# e para cada número digitado imprima na tela se o número é negativo, positivo ou zero.

quant = int(input("Quantos números você irá digitar?\n"))
cont = 0

while cont < quant:
    numero = int(input("Digite um valor:"))
    if numero == 0:
        print("Zero")
    elif numero > 0:
        print("Positivo")
    else:
        print("Negativo")
    cont += 1
