a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor (deve ser maior do que o primeiro): "))

while (a >= b):
    print("O Segundo valor deve ser MAIOR do que o primeiro valor digitado.")
    b = float(input("Digite o segundo valor (deve ser maior do que o primeiro): "))

print(f'O segundo valor digitado ({b}) é maior do que o primeiro valor digitado {a}.')