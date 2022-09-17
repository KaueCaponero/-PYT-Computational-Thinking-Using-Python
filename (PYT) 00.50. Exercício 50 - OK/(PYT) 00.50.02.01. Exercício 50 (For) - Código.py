a = int(input("Digite o número inicial do intervalo: "))
b = int(input("Digite o número final do intervalo: "))

for a in range (a, (b+1), 1):
    if (a >= 10):
        if (a % 2 == 0):
            print(a)
print("São os números pares no intervalo informado.")
print("Programa Encerrado")