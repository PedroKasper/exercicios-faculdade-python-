# Crie um programa que solicita para o usuário que ele digite 10 valores inteiros.
# Ao final, imprima a soma de todos os valores digitados.

i = 0
soma = 0

while i < 10:
    valor = int(input("Digite um valor inteiro:"))
    soma += valor
    i += 1

print("Soma dos valores: ", soma)
