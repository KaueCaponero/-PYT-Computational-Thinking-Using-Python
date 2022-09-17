x = int(input("Digite o início do intervalo: "))
y = int(input("Digite o final do intervalo: "))

while (y <= x):
    print("O valor final deve ser maior do que o valor inicial.")
    y = int(input("Digite o final do intervalo: "))

soma = 0

for x in range(x,(y+1),1):
    soma = soma + x

print(f"A soma dos valores do intervalo é: {soma}")
