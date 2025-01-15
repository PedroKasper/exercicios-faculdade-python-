# Uma disciplina possui Grau A e Grau B. A nota do Grau A vale
# 33% da nota final, enquanto a nota do Grau B vale 67% da
# nota final. O Grau A possui as seguintes avaliações:
# – Atividade prática: 45% da nota do Grau A
# – Atividade teórica: 55% da nota do Grau A
# Já o Grau B possui as seguintes avaliações:
# – Prova em laboratório: 60% da nota do Grau B
# – Teste teórico: 20% da nota do Grau B
# – Trabalho extraclasse: 20% da nota do Grau B
# Crie um programa que solicite as notas de todas as avaliações e
# imprime na tela a nota final obtida na disciplina.

graua1 = float(input("Digite a nota da atividade prática do grau A:"))
graua2 = float(input("Digite a nota da atividade teórica do grau A:"))
graub1 = float(input("Digite a nota da prova em laboratório do grau B:"))
graub2 = float(input("Digite a nota do teste teórico do grau B:"))
graub3 = float(input("Digite a nota do trabalho extraclasse do grau B:"))

notaGrauA = (graua1*0.45) + (graua2*0.55)
notaGrauB = (graub1*0.6) + (graub2*0.2) + (graub3*0.2)

notaFinal = (notaGrauA*0.33) + (notaGrauB*0.67)

print("Sua nota final é:", notaFinal)
