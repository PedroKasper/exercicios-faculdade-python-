# Crie um programa que permita que o usuário crie sua lista de compras.
# Primeiramente, solicite que ele informe quantos produtos serão adicionados na lista.
# Depois disto, peça para que o usuário digite os produtos que ele vai comprar, e armazene em uma lista.
# Ao final, imprima a lista de compras do usuário.

lista = []

quant = int(input("Quantos produtos serão adicionados a lista?\n"))

for i in range(0, quant):
    produto = input("Digite um produto:")
    lista.append(produto)

print(lista)
