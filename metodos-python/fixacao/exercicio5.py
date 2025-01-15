# Crie um método que recebe um valor por parâmetro (assuma que será inteiro) e retorna
# a soma de todos os valores entre 0 e o valor recebido.
# Caso o valor seja negativo, o método deve retornar -1.

def somadosValores(a):
    if a < 0:
        return -1
    else:
        soma = 0
        for i in range(0, a):
            soma += i
        return soma


valor = somadosValores(-4)
print(valor)
