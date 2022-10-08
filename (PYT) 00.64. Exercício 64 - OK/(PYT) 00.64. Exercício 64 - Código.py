numeros = []
i = 0
nulo = 0
par = 0
impar = 0

qtdnum = int(input("Quanto valores quer comparar? (Máximo de 20): "))

while (qtdnum < 0  or qtdnum > 20):
    print("Valor Inválido.")
    qtdnum = int(input("Quanto valores quer comparar? (Máximo de 20): "))

for i in range (0,qtdnum,1):
    indice = i + 1
    numeros.append(int(input(f"Digite o {indice}º número: ")))
    if (numeros[i] == 0):
        nulo = nulo + 1
    elif (numeros[i] % 2 == 0):
        par = par + 1
    else:
        impar = impar + 1

percentpar = (par / qtdnum)*100
percentimpar = (impar / qtdnum)*100
percentnulo = (nulo / qtdnum)*100

print(f"Valores pares: {par} número(s). {percentpar:.2f} % do total")
print(f"Valores ímpares: {impar} número(s). {percentimpar:.2f} % do total")
print(f"Valores nulos (0): {nulo} número(s). {percentnulo:.2f} % do total")