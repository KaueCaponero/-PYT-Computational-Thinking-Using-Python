n = int(input("Digite o termo que quer encontrar (valor deve ser positivo e menor que 50): "))

while (n <= 0) or (n > 50):
    print("O valor de N deve ser positivo e menor que 50.")
    n = int(input("Digite o termo que quer encontrar (valor deve ser positivo e menor que 50): "))

dividendo = 1
divisor = 2
soma = 0

for i in range(1, (n + 1), 1):
    divisao = dividendo / divisor
    soma = soma + divisao
    print(f"{i}. {dividendo}/{divisor}")
    dividendo = dividendo + 1
    divisor = divisor + 1

print("A soma é: %.2f" % soma)