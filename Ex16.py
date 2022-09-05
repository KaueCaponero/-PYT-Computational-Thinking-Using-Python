#cadj = float(input("Digite o valor do cateto adjacente: "))
#cops = float(input("Digite o valor do cateto oposto: "))
#hipt = float(input("Digite o valor da hipotenusa: "))

#if ( (cadj ** 2) + (cops ** 2) == (hipt ** 2) ):
    #print("O Triângulo informado é um triângulo retângulo!")

#else:
    #print("O Triângulo informado não é um triângulo retângulo.")


a = float(input("Digite o valor do primeiro lado: "))
b = float(input("Digite o valor do segundo lado: "))
c = float(input("Digite o valor do terceiro lado: "))

if (a > b) and (a > c):
    hipt = a
    l1 = b
    l2 = c

elif (b > a) and (b > c):
    hipt = b
    l1 = a
    l2 = c

else:
    hipt = c
    l1 = a
    l2 = b

if ( (l1 ** 2) + (l2 ** 2) == (hipt ** 2)):
    print("O Triângulo informado é um triângulo retângulo!")

else:
    print("O Triângulo informado não é um triângulo retângulo.")