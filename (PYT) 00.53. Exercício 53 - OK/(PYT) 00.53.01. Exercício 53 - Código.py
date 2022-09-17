numeros = []

for i in range(0,20,1):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

c = 2

for i in range(0,20,1):
    numeros[i] = numeros[i] * c

print(numeros)