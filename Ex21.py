novocalculo = 1

while (novocalculo == 1):

    a = float(input("Digite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))

    operador = int(input("Escolha o operador lógico abaixo (digite o número correspondente): \n1. X \n2. + \n3. / \n4. - \n5. Sair \n"))

    if (operador == 1):
            result = a * b
            print("O resultado do cálculo é: ", result)
    elif (operador == 2):
            result = a + b
            print("O resultado do cálculo é: ", result)
    elif (operador == 3):
            if (b == 0):
                print("Não é possível dividir por 0.")
            else:
                result = a / b
                print("O resultado do cálculo é: ", result)
    elif (operador == 4):
            result = a - b
            print("O resultado do cálculo é: ", result)
    elif (operador == 5):
            print("Programa Encerrado")
            break
    else:
            print("Operador inválido.")

    novocalculo = int(input("Deseja efetuar novo cálculo? (digite o número correspondente): \n1. Sim \n2. Não \n"))

else:
    print("Programa Encerrado.")