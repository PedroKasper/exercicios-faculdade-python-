# Crie um programa que solicita o time de 10 usuários pelo teclado.
# Ao final, imprima quantos torcedores torcem para o Grêmio.

cont_gremio = 0
cont = 0

while cont < 10:
    time = input("Digite o time de futebol que você torce: ")

    if time.lower() == "gremio":
        cont_gremio += 1

    cont += 1

print("Total de torcedores do Grêmio:", cont_gremio)
