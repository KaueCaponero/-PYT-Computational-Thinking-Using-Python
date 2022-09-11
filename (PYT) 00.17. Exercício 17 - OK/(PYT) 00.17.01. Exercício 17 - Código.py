peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
sexo = input("Digite o seu sexo (m ou f): ")

imc = peso / (altura ** 2)

if (sexo == "m"):
    if (imc < 20):
        print("Seu imc é de %.2f. Você está abaixo do peso ideal." %imc)

    elif (imc < 25):
        print("Seu imc é de %.2f. Você no peso ideal." %imc)

    else:
        print("Seu imc é de %.2f. Você está acima do peso ideal." %imc)

else:
    if (imc < 19):
        print("Seu imc é de %.2f. Você está abaixo do peso ideal." %imc)

    elif (imc < 24):
        print("Seu imc é de %.2f. Você no peso ideal." %imc)

    else:
        print("Seu imc é de %.2f. Você está acima do peso ideal." %imc)