n = int(input("Digite o termo que quer encontrar (valor deve ser positivo e menor que 50): "))

while (n <= 0) or (n > 50):
    print("O valor de N deve ser positivo e menor que 50.")
    n = int(input("Digite o termo que quer encontrar (valor deve ser positivo e menor que 50): "))

i = 1
soma = 0

while (i <= n):
    dividendo = (i ** 2) + 1
    divisor = (i ** 3)
    divisao = dividendo / divisor
    print(f"{i}. {dividendo} / {divisor}")
    i = i + 1
    soma = soma + divisao

print('A soma é: %.2f' %soma)