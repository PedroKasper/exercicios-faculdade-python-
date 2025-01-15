# Crie um programa que recebe um valor inteiro referente a um determinado ano.
# Imprima na tela se o ano informado é bissexto ou não.

ano = int(input("Digite um ano:"))

if ano % 4 == 0:
    print("Ano bissexto!")
else:
    print("Ano não bissexto!")
