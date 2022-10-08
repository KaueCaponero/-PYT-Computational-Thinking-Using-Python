vetor = []
indice = 1

for i in range (0,20,1):
    vetor.append(int(input(f"Digite o {indice}º número: ")))
    indice = indice + 1

    if (i == 0):
        menor = vetor[i]
    
    else:
        for j in range (0,i,1):
            if (vetor[i] < vetor[j]):
                menor = vetor[i]
                prox = vetor[j]
                vetor[j] = menor
                vetor[i] = prox

print(vetor)


"""
Correção:

numeros = []

for i in range (0,5,1):
    num = input("Digite um número")
    numeros.append(num)

for i in range (0,5,1):
    for j in range (i+1,5,1):
        if (numeros[i] < numeros[j]):
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

for i in range (0,5,1):
    print(numeros[i])

"""