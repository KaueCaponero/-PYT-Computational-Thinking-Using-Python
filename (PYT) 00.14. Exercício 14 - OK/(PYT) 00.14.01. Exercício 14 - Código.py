peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em m): "))

imc = peso / (altura ** 2)

if (imc < 19):
    print("Seu imc é de %.2f. Você está abaixo do peso ideal." %imc)

elif (imc >= 19) and (imc < 24):
    print("Seu imc é de %.2f. Você está no peso ideal." %imc)

else:
    print("Seu imc é de %.2f. Você está acima do peso ideal." %imc)