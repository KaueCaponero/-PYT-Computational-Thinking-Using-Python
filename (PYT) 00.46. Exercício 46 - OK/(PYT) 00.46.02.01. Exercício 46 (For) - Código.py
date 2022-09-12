novocalculo = "S"

while (novocalculo.upper() == "S"):

    n = int(input("Digite a quantidade de números a ser comparada (deve ser maior que 0 e menor que 20): "))

    while (n <= 0) or (n >= 20):
        print("Valor inválido.")
        n = int(input("Digite a quantidade de números a ser comparada (deve ser maior que 0 e menor que 20): "))

    xpos = 0
    xneg = 0
    xnul = 0
    soma = 0
    maior = 0
    menor = 0

    for i in range(1, (n + 1), 1):
        x = int(input(f"Digite o {i}º número: "))

        if (i == 1):
            maior = x
            menor = x
            if (x > 0):
                xpos = xpos + 1
            elif (x < 0):
                xneg = xneg + 1
            else:
                xnul = xnul + 1
        elif (x > maior):
            maior = x
            if (x > 0):
                xpos = xpos + 1
            elif (x < 0):
                xneg = xneg + 1
            else:
                xnul = xnul + 1
        elif (x < menor):
            menor = x
            if (x > 0):
                xpos = xpos + 1
            elif (x < 0):
                xneg = xneg + 1
            else:
                xnul = xnul + 1
        else:
            if (x > 0):
                xpos = xpos + 1
            elif (x < 0):
                xneg = xneg + 1
            else:
                xnul = xnul + 1
        
        soma = soma + x  

    media = soma / n
    porcpos = (100 * xpos) / n
    porcneg = (100 * xneg) / n
    porcnul = (100 * xnul) / n

    print('O maior valor é: %.2f' %maior)
    print('O menor valor é: %.2f' %menor)
    print('A soma dos valores é: %.2f' %soma)
    print('A média dos valores é: %.2f' %media)
    print('A porcentagem de valores positivos é: %.2f' %porcpos)
    print('A porcentagem de valores negativos é: %.2f' %porcneg)
    print('A porcentagem de valores nulos (0) é: %.2f' %porcnul)

    novocalculo = input("Deseja calcular novamente? (S ou N): ")

    while (novocalculo.upper() != 'S') and (novocalculo.upper() != 'N'):
        print("Favor responder com S para SIM ou N para NÃO")
        novocalculo = input("Deseja calcular novamente? (S ou N): ")

print("Programa Encerrado.")

