a = int(input("Digite um número:\n"))

if ( a == 0 ):
    print("O valor digitado é nulo (0).")
elif ((a % 2) == 0):
    result = a + 5
    print("O valor digitado (",a,") é par, portanto",a,"+ 5 =",result)
else:
    result= a + 8
    print("O valor digitado (",a,") é ímpar, portanto",a,"+ 8 =",result)
    