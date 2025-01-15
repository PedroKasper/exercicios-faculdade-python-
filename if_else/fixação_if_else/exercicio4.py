# Crie um programa que recebe três valores inteiros pelo teclado e imprime qual dos três é menor.

a = int(input("Digite um valor:"))
b = int(input("Digite um valor:"))
c = int(input("Digite um valor:"))

if a < b and a < c:
    print(a, "é o menor valor")
elif b < a and b < c:
    print(b, "é o menor valor")
else:
    print(c, "é o menor valor")
