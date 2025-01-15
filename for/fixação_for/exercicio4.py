# Sabendo que uma string é uma lista de letras, peça para o usuário digitar um texto e imprima na tela
# a quantidade de vogais que existem no texto.

texto = input("Digite qualquer texto:")

vogais = 0

minusculas = texto.lower()

for letra in minusculas:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vogais += 1

print("Número de vogais:", vogais)
