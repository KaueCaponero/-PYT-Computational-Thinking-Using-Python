soma = 0

for i in range(1, 11, 1):
    n = int(input(f"Digite o {i}º número: "))

    while (n < 0):
        print("O número deve ser positivo!")
        n = int(input(f"Digite o {i}º número positivo: "))

    if (i == 1):
        maior = n
    elif (n > maior):
        maior = n

    soma = soma + n
   
media = soma / i

print(f'O maior valor é: {maior}')
print(f'A soma dos valores é: {soma}')
print(f'A média dos valores é: {media}')