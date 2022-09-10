"""
i = 1
soma = 0

while (i <= 10):
    n = int(input(f"Digite o {i}º número: "))

    if (i == 1):
        maior = n
    elif (maior > n):
        maior = n

    soma = soma + n
    i = i + 1

media = soma / i

print(f'O maior valor é: {maior}')
print(f'A soma dos valores é: {soma}')
print(f'A média dos valores é: {media}')
"""