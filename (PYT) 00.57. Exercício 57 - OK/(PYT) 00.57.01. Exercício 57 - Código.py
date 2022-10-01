nome = []
idade = []
sexo = []

for i in range(0,10,1):

    nome.append(input("Digite seu nome: "))
    
    id = int(input("Digite sua idade: "))
    while (id < 0):
        print("Idade Inválida.")
        id = int(input("Digite sua idade: "))

    idade.append(id)

    sx = input("Digite seu sexo (M ou F): ")
    while (sx.upper() != "M" and sx.upper() != "F"):   
        print("Sexo Inválido")
        sx = input("Digite seu sexo (M ou F): ")

    sexo.append(sx.upper())

print("As pessoas do sexo Feminino são: ")
for i in range (0,10,1):
    if sexo[i] == "F":
        print("Nome: ", nome[i], "| Sexo:", sexo[i], "| Idade: ", idade[i])