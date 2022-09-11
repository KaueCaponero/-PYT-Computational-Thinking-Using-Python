sexo = input("Qual o seu sexo? (Use M para masculino e F para feminino): ")

while (sexo.upper() != "M" and sexo.upper() != "F"):
    print("Sexo inválido.")
    sexo = input("Qual o seu sexo? (Use M para masculino e F para feminino): ")

if (sexo.upper() == "M"):
    print("Você é do sexo masculino.")
else:
    print("Você é do sexo feminino.")