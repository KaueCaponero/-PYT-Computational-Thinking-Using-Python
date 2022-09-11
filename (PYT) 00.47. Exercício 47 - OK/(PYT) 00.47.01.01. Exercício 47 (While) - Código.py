novocalculo = "S"

while (novocalculo.upper() == "S"):
    fatorial = 1
    x = int(input("Digite o número (positivo) que você quer calcular o fatorial: "))
    x1 = x

    while (x < 0):
        print("O valor deve ser positivo.")
        x = int(input("Digite o número (positivo) que você quer calcular o fatorial: "))
        x1 = x

    if (x == 0):
        print("0! = 1")
        novocalculo = input("Deseja calcular novamente? (S ou N): ")

        while (novocalculo.upper() != 'S') and (novocalculo.upper() != 'N'):
            print("Favor responder com S para SIM ou N para NÃO")
            novocalculo = input("Deseja calcular novamente? (S ou N): ")
        
    else:
        while (x > 0):
            fatorial = fatorial * x
            x = x - 1

        print(f'{x1}! = {fatorial}')

        novocalculo = input("Deseja calcular novamente? (S ou N): ")

        while (novocalculo.upper() != 'S') and (novocalculo.upper() != 'N'):
            print("Favor responder com S para SIM ou N para NÃO")
            novocalculo = input("Deseja calcular novamente? (S ou N): ")

print("Programa Encerrado.")