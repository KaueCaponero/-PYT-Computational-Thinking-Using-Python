n = int(input("Digite o termo que quer encontrar (valor deve ser positivo e menor que 50): "))

while (n <= 0) or (n > 50):
    print("O valor de N deve ser positivo e menor que 50.")
    n = int(input("Digite o termo que quer encontrar (valor deve ser positivo e menor que 50): "))

soma = 0

for i in range(1, (n+1), 1):
    dividendo = (i ** 2) + 1
    divisor = (i ** 3)
    divisao = dividendo / divisor
    print(f"{i}. {dividendo} / {divisor}")
    soma = soma + divisao

print('A soma é: %.2f' %soma)