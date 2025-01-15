# Crie um programa que solicita o nome e o estado civil de 20 pessoas pelo teclado.
# Ao final, imprima apenas o nome das pessoas separadas por estado civil:
# solteiras, casadas, divorciadas e viúvas (nesta ordem!)

solteiras = []
casadas = []
viuvas = []
divorciadas = []

for i in range(0, 20):

    nome = input("Digite seu nome:")

    estadoCivil = input("Digite seu estado civil:")

    if (estadoCivil == "solteiro" or estadoCivil == "solteira"):
        solteiras.append(nome)

    elif (estadoCivil == "casado" or estadoCivil == "casada"):
        casadas.append(nome)

    elif (estadoCivil == "viúvo" or estadoCivil == "viúva"):
        viuvas.append(nome)

    elif (estadoCivil == "divorciado" or estadoCivil == "divorciada"):
        divorciadas.append(nome)

    else:
        print("[ERRO] Estado civil inválido!")


print("Pessoas viúvas:")

print(viuvas)


print("Pessoas casadas:")

print(casadas)


print("Pessoas solteiras:")

print(solteiras)


print("Pessoas divorciadas:")

print(divorciadas)
