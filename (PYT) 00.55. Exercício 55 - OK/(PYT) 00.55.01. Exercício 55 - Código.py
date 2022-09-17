min = 1
max = 20

qtdnum = int(input(f"Digite a quantidade de valores que quer armazenar (de {min} a {max} números): "))

while (qtdnum < min) or (qtdnum > max):
    print(f"Quantidade inválida. Deve ser entre {min} e {max} números.")
    qtdnum = int(input("Digite a quantidade de valores que quer armazenar (máximo de 20 números): "))

numeros = []

for i in range(0, qtdnum, 1):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

consultar = "S"

while (consultar.upper() == "S"):

    busca = int(input("Digite o valor que quer encontrar a posição no array: "))

    encontrados = []

    for i in range(0, qtdnum, 1):
        if (busca == numeros[i]):
            encontrados.append(int(i))
        else:
            continue

    if encontrados == []:
        print("Valor não encontrado.")
    else:
        print(f"O número buscado {busca} está na(s) posição(ões) {encontrados} do array.")

    consultar = input("Deseja consultar novamente? (S para SIM e N para NÃO): ")

    while consultar.upper() != "N" and consultar.upper() != "S":
        print("Resposta Inválida.")
        consultar = input("Deseja consultar novamente? (S para SIM e N para NÃO): ")

print("Programa Encerrado.")