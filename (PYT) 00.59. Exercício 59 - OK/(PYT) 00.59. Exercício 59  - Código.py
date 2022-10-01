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

contador = 0

print("As pessoas com idade acima de 18 anos são: ")
for i in range (0,10,1):
    if idade[i] > 18:
        print("Nome: ", nome[i], "| Sexo:", sexo[i], "| Idade: ", idade[i])
        contador = contador + 1
        input("Pressione qualquer tecla para seguir.\n")

print("O número total de pessoas é de: ", contador)