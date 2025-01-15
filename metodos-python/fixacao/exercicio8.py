# Crie um método que recebe uma lista por parâmetro (assuma que será uma lista de string)
# e retorna a menor string da lista (com menos caracteres).

def menor_string_usuario():
    entrada = input("Digite os elementos da lista separados por vírgula: ")
    lista = entrada.split(',')

    menor = lista[0]
    for string in lista:
        if len(string.strip()) < len(menor.strip()):
            menor = string.strip()
    return menor


menor = menor_string_usuario()
print(menor)
