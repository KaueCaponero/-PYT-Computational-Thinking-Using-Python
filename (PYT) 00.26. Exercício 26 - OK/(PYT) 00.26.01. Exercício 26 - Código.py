a = float(input("Digite um número: "))

if (a > 0):
    result = a * 2
    print(a,"é positivo, portanto seu dobro vale",result)
elif (a < 0):
    result = a * 3
    print(a,"é negativo, portanto seu triplo vale",result)
else:
    print("O valor digitado é 0.")
