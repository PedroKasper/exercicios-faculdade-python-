# Crie um método que recebe dois valores val1 e val2 (assuma que serão inteiros).
# O método deve retornar verdadeiro se val1 for divisível por val2 e falso caso contrário.

def valores(val1, val2):
    if val1 % val2 == 0:
        return True
    else:
        return False


resultado = valores(7, 2)
# if resultado:
#    print("Divisível!")
# else:
#    print("Não divisível!")
