# Crie um programa que recebe o preço de um produto pelo teclado e imprime
# na tela a mensagem adequada, de acordo com o preço:
# “Preço inválido”, se o preço for negativo ou zero
# “Preço baixo”, se o preço for entre 0 e 30 (inclusive)
# “Preço médio”, se o preço for entre 30 e 50 (inclusive)
# “Preço alto”, se o preço for maior do que 50

valor = float(input("Digite o preço do produto:"))

if valor <= 0:
    print("Preço inválido")
elif valor > 1 and valor <= 30:
    print("Preço baixo")
elif valor > 30 and valor <= 50:
    print("Preço médio")
else:
    print("Preço alto")
