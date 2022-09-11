novocalculo = "S"

while (novocalculo.upper() == "S"):

    n = int(input("Quantos números você irá digitar? (1 até 19) "))

    while ( n < 1 or n > 19):
        print("Número inválido. O número digitado deve estar entre 1 e 19.")
        n = int(input("Quantos números você irá digitar? (1 até 19) "))

    i = 1
    soma = 0
    xneg = 0
    xpos = 0
    maior = 0
    menor = 0
    x0 = 0

    while (i <= n):
        x = int(input(f'Digite o {i}º número: '))

        if (x < 0):
            xneg = xneg + 1
            if (x < menor):
                menor = x
            elif (x > maior):
                maior = x

        elif (x > 0):
            xpos = xpos + 1
            if (x < menor):
                menor = x
            elif (x > maior):
                maior = x

        else:
            x0 = x0 + 1
        
        soma = soma + x
        i = i + 1

    media = soma / n
    porcneg = 100 * xneg / n
    porcpos = 100 * xpos / n
    porcnul = 100 * x0 / n

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

