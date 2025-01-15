# Crie um programa que aplica uma taxa de juros em um determinado preço digitado pelo teclado.
# A taxa aplicada deve ser:
# Aumento de 10% caso o valor seja menor do que 100
# Aumento de 20% caso o valor esteja entre 100 (inclusive) e 300
# Aumento de 50% caso o valor esteja entre 300 (inclusive) e 1000
# Imprima uma mensagem de erro se o valor for negativo
# Ao final, seu programa deve imprimir o novo valor, já com a taxa aplicada.

valor = float(input("Digite o preço do produto:"))

if valor < 100 and valor > 0:
    print("O valor com juros fica", (valor + (valor * 0.1)))
elif valor >= 100 and valor < 299:
    print("O valor com juros fica", (valor + (valor * 0.2)))
elif valor >= 300 and valor < 999:
    print("O valor com juros fica", (valor + (valor * 0.5)))
elif valor < 0:
    print("Erro: Valor negativo!")
