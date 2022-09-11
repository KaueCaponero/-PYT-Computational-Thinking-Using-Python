n = int(input("Digite o termo que quer encontrar (valor deve ser positivo e menor que 100): "))

while (n <= 0) or (n > 100):
    print("O valor de N deve ser positivo e menor que 100.")
    n = int(input("Digite o termo que quer encontrar (valor deve ser positivo e menor que 100): "))

soma = 0

for i in range (1, (n+1), 1):
    termo = (i ** 2) + 1
    soma = soma + termo
    print(f"{i}. {termo}")
    
print(f'A soma é: {soma}')