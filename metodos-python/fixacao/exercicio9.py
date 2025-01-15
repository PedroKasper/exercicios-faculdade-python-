# Crie um método que recebe dois parâmetros, que serão um inteiro N e uma string S (nesta ordem).
# O método deve imprimir na tela N vezes a string S.

def recebeValores():
    n = int(input("Digite um inteiro:"))
    s = input("Digite uma string:")

    for i in range(0, n):
        print(s)


recebeValores()
