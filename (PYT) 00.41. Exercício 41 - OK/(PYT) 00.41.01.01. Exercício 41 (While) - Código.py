n = int(input("Digite o termo que quer encontrar (valor deve ser positivo e menor que 100): "))

while (n <= 0) or (n > 100):
    print("O valor de N deve ser positivo e menor que 100.")
    n = int(input("Digite o termo que quer encontrar (valor deve ser positivo e menor que 100): "))

i = 1
soma = 0

while (i <= n):
    termo = (i ** 2) + 1
    print(f"{i}. {termo}")
    i = i + 1
    soma = soma + termo

print(f'A soma é: {soma}')