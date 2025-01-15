# Crie um método chamado maiorValor que recebe 3 valores por parâmetro
# (assuma que serão inteiros) e retorna o maior dos três valores.

def maiorValor(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


maior = maiorValor(12, 6, 7)
print(maior)
