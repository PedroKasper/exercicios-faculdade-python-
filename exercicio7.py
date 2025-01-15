# Uma determinada disciplina possui apenas
# 3 avaliações: o trabalho (que vale 10% da
# nota), a prova (que vale 60% da nota) e o
# teste (que vale 30% da nota). Crie um
# programa que pede para o usuário digitar
# as notas que ele tirou nestas avaliações e
# imprime na tela a nota final do aluno.

trabalho = float(input("Digite a nota do trabalho:"))
teste = float(input("Digite a nota do teste:"))
prova = int(input("Digite a nota da prova:"))

notaFinal = (trabalho*0.1)+(teste*0.3)+(prova*0.6)

print("A nota final é", notaFinal)
