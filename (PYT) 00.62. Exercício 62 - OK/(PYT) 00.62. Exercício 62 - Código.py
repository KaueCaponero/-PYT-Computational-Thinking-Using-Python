i = 0
qtdpessoas = 20
nome = []
sexo = []
idade = []

for i in range (0,qtdpessoas,1):
    indice = i + 1

    nome.append(input(f"{indice}. Digite seu nome: "))

    sx = input(f"{indice}. Digite seu sexo: (M ou F): ").upper() 
    while (sx != "M" and sx != "F"):
        print("Sexo Inválido.")
        sx = input(f"{indice}. Digite seu sexo: (M ou F): ").upper()
    
    sexo.append(sx)

    idade.append(int(input(f"{indice}. Digite sua idade: ")))

for i in range (0,qtdpessoas,1):
    for j in range (i+1,qtdpessoas,1):
        if (idade[i] < idade[j]):
            auxIdade = idade[i]
            idade[i] = idade[j]
            idade[j] = auxIdade

            auxNome = nome[i]
            nome[i] = nome[j]
            nome[j] = auxNome

            auxSexo = sexo[i]
            sexo[i] = sexo[j]
            sexo[j] = auxSexo

i = 0
indice = 0

print("Pessoas cadastradas: ")

for i in range (0,qtdpessoas,1):
    indice = i + 1
    print(f"{indice}. Nome: {nome[i]} - Sexo: {sexo[i]} - Idade: {idade[i]}")




