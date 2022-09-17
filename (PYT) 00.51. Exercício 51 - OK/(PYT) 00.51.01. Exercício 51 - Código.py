numeros = []

for i in range(0,10,1):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

for i in range(9,-1,-1):
    print(f"O {i+1}º número digitado foi: {numeros[i]}")