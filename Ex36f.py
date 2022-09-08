x = int(input("Digite um valor positivo que queira calcular a tabuada: "))

while (x <= 0):
    print("Valor inválido. Digite um valor POSITIVO.")
    x = int(input("Digite um valor positivo que queira calcular a tabuada: "))

a = int(input("Digite o início do intervalo que quer calcular a tabuada: "))
b = int(input("Digite o fim do intervalo que quer calcular a tabuada: "))

while (b <= a):
    print(f"O fim do intervalo ({b}) deve ser maior do que o início do intervalo ({a}).")
    c = int(input("Digite o fim do intervalo que quer calcular a tabuada: "))

i = b

for i in range(b,(a-1),-1):
    tab = x * i
    print(tab)
    i = i - 1