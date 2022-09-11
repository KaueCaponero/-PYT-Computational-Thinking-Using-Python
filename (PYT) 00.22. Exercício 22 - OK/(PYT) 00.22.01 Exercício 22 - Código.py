novocalculo = 1

while (novocalculo == 1):
    figura = int(input("Escolha a figura que quer calcular a área: \n1. Triângulo\n2. Quadrado\n3. Retângulo\n4. Círculo\n5. Sair\n"))

    if (figura == 1):
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        area = (base * altura) / 2
        print("A área do triângulo informado é: ", area, "\n")
    elif (figura == 2):
        lado = float(input("Digite o lado do quadrado: "))
        area = lado ** 2
        print("A área do quadrado informado é: ", area, "\n")
    elif (figura == 3):
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = (base * altura)
        print("A área do retângulo informado é: ", area, "\n")
    elif (figura == 4):
        pi = 3.1416
        raio = float(input("Digite o raio do círculo: "))
        area = (pi * (raio ** 2))
        print("A área do círculo informado é: ", area, "\n")
    elif (figura == 5):
        print("Programa Encerrado.")
        break
    else:
        print("Figura inválida.")
    
    novocalculo = int(input("Deseja efetuar novo cálculo? (digite o número correspondente): \n1. Sim \n2. Não \n"))

else:
    print("Programa Encerrado.")