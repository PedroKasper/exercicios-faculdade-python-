# Crie um programa que recebe dois valores inteiros pelo teclado e imprime qual dos dois é maior.

a = int(input("Digite um valor:"))
b = int(input("Digite um valor:"))

if a > b:
    print("Maior valor:", a)
elif b > a:
    print("Maior valor:", b)
elif a == b:
    print("Os valores são iguais")
