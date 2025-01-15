# Crie um programa que pede para o usuário digitar 20 números com ponto flutuante pelo teclado.
# Ao final, seu programa deve imprimir todos os números digitados.

numeros_string = " "
i = 0

while i < 20:
    numero = input("Digite um número:")
    numeros_string += numero + " "
    i += 1

print("Números digitados:", numeros_string)
