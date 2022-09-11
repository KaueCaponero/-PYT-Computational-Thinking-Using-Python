i = 1
soma = 0

while (i <= 10):
    n = int(input(f"Digite o {i}º número positivo: "))

    while (n < 0):
        print("O número deve ser positivo!")
        n = int(input(f"Digite o {i}º número positivo: "))

    if (i == 1):
        maior = n
    elif (n > maior):
        maior = n

    soma = soma + n
    i = i + 1

media = soma / (i - 1)

print(f'O maior valor é: {maior}')
print(f'A soma dos valores é: {soma}')
print(f'A média dos valores é: {media}')
