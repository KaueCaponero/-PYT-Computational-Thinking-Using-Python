novocalculo = 1

while (novocalculo ==1):


    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    if (a + b < c):
        print(a, "+", b, "<", c, "portanto o valor de A + B é menor que C.\n")
    else:
        print(a, "+", b, "não é <", c, "portanto o valor de A + B não é menor que C.\n")

    novocalculo = int(input("Deseja efetuar novo cálculo? (digite o número correspondente): \n1. Sim \n2. Não \n"))

else:
    print("Programa Encerrado.")