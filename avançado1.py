# Faça um programa em Python que:
# – Receba um float digitado pelo usuário e armazena em A
# – Receba um inteiro digitado pelo usuário e armazene em B
# – Imprima as seguintes mensagens na tela (substitua o X e o Y pelo
# resultado da operação indicada na mensagem):
# • “A multiplicado por B é X”
# • “A dividido por B é X”
# • “A mais B é X e A menos B é Y”
# • “A elevado a B é X”

a = float(input("Digite o valor de A:"))
b = int(input("Digite o valor de B:"))

multiplica = a*b
divide = a/b
soma = a+b
dimunui = a-b
eleva = a ** b

print("A multiplicado por B é", multiplica)
print("A dividido por B é", divide)
print("A mais B é", soma, "e A menos B é", dimunui)
print("A elevado a B é", eleva)
