# Crie um método que recebe um valor por parâmetro (assuma que será uma string)
# e retorna a quantidade de letras que existem neste texto.

def contarLetras(string):
    quantidade = sum(caractere.isalpha() for caractere in string)
    return quantidade


texto = input("Digite um texto:")
quantidadeLetras = contarLetras(texto)
print(quantidadeLetras)
