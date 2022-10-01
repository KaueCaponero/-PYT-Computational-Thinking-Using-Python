nome = []
idade = []

for i in range(0,10,1):
    nome.append(str(input("Digite seu nome: ")))
    idade.append(int(input("Digite sua idade: ")))

for i in range (0,10,1):
    print("Nome: ", nome[i], " Idade: ", idade[i])