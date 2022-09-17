numeros = []

for i in range(0,10,1):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))
    if (i == 0):
        maior = numeros[i]
        imaior = i+1
    elif (numeros[i] > maior):
        maior = numeros[i]
        imaior = i+1

print(f"O maior valor digitado foi o {imaior}º: {maior}")
