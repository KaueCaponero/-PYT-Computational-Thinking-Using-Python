print("Programa de Triângulos")

a = float(input("Digite o primeiro lado do triângulo: "))
b = float(input("Digite o segundo lado do triângulo: "))
c = float(input("Digite o terceiro lado do triângulo: "))

#Verifica se é um triângulo
if ( ((a + b) > c) and ((a + c) > b) and ((b + c) > a) ):
    if ( (a==b) and (b==c)):
        print("Triângulo equilátero!")

    elif ( (a!=b) and (a!=c) and (b!=c)):
        print("Triângulo escaleno!")
    
    else:
        print("Triângulo isóceles!")

else:
    print("Não é um triângulo!")