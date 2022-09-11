a = int(input("Digite o valor positivo que quer calcular a tabuada: "))

while (a <= 0):
    print("Valor inválido, favor digitar um valor POSITIVO;")
    a = int(input("Digite o valor positivo que quer calcular a tabuada: "))

i = 1

while (i <= 10):
    tab = a * i
    print(tab)
    i = i + 1
