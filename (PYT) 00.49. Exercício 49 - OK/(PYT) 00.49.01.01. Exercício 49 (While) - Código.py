x = int(input("Digite o início do intervalo: "))
y = int(input("Digite o final do intervalo: "))

while (y <= x):
    print("O valor final deve ser maior do que o valor inicial.")
    y = int(input("Digite o final do intervalo: "))

soma = 0

while (x <= y):
    soma = soma + x
    x = x + 1

print(f"A soma dos valores do intervalo é: {soma}")
