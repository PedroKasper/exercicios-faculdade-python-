# Crie um programa que pede 5 números inteiros pelo
# teclado e armazena-os, respectivamente, nas variáveis
# A, B, C, D e E. Em seguida, faça o que se pede:
# – sabendo que B e C são respectivamente a base e a altura de
# um triângulo, imprima a área deste triângulo
# – sabendo que A, B, C e D formam um retângulo, imprima o
# perímetro deste retângulo
# – sabendo que E é o valor do raio de um determinado círculo,
# imprima a área deste círculo

import math


a = int(input("Digite uma valor para a:"))
b = int(input("Digite uma valor para b:"))
c = int(input("Digite uma valor para c:"))
d = int(input("Digite uma valor para d:"))
e = int(input("Digite uma valor para e:"))

triangulo = ((b*c)/2)
print("A área do triângulo é:", triangulo)

retangulo = (a+b+c+d)
print("O perímetro do retângulo é:", retangulo)

circulo = (math.pi * ((e) ** 2))
print("A área do círculo é:", circulo)
