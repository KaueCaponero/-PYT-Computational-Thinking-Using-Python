a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if ( (a < b) & (a < c)):
    if (b < c):
        print("Ordem Decrescente: \n1. ",c,"\n2. ",b,"\n3. ",a)
    else:
        print("Ordem Decrescente: \n1. ",b,"\n2. ",c,"\n3. ",a)
elif ( (b < a) & (b < c)):
    if (a < c):
        print("Ordem Decrescente: \n1. ",c,"\n2. ",a,"\n3. ",b)
    else:
        print("Ordem Decrescente: \n1. ",a,"\n2. ",c,"\n3. ",b)
else:
    if (a < b):
        print("Ordem Decrescente: \n1. ",b,"\n2. ",a,"\n3. ",c)
    else:
        print("Ordem Decrescente: \n1. ",a,"\n2. ",b,"\n3. ",c)