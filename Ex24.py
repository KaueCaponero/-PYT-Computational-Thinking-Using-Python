nome = str(input("Digite o seu nome: "))
sexo = str(input("Digite o seu sexo (M ou F): "))
estadocivil = int(input("Selecione seu estado civil (digite o número correspondente): \n1. Solteiro(a) \n2. Casado(a) \n3. Separado(a)\n4. Divorciado(a)\n5. Viúvo(a)\n"))

if (sexo == "F"):
        if (estadocivil == 1):
            estciv = str("solteira")
            print(nome," é do sexo feminino e é",estciv)
        elif (estadocivil == 2):
            estciv = str("casada")
            tempocasada = int(input("Há quanto tempo você é casada? (em anos)\n"))
            print(nome,"é do sexo feminino e é casada há",tempocasada, "anos.")
        elif (estadocivil == 3):
            estciv = str("separada")
            print(nome," é do sexo feminino e é",estciv)
        elif (estadocivil == 4):
            estciv = str("divorciada")
            print(nome," é do sexo feminino e é",estciv)
        elif (estadocivil == 5):
            estciv = str("viúva")
            print(nome," é do sexo feminino e é",estciv)
        else:
            ("Estado civil inválido.")
elif (sexo == "M"):
        if (estadocivil == 1):
            estciv = str("solteiro")
            print(nome,"é do sexo masculino e é",estciv)
        elif (estadocivil == 2):
            estciv = str("casado")
            print(nome,"é do sexo masculino e é",estciv)
        elif (estadocivil == 3):
            estciv = str("separado")
            print(nome,"é do sexo masculino e é",estciv)
        elif (estadocivil == 4):
            estciv = str("divorciado")
            print(nome,"é do sexo masculino e é",estciv)
        elif (estadocivil == 5):
            estciv = str("viúvo")
            print(nome,"é do sexo masculino e é",estciv)
        else:
            ("Estado civil inválido.")
else:
    print("O sexo digitado é inválido.")
    