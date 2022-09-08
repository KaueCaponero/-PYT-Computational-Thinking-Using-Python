preco = float(input("Digite o preço do produto: "))
parcelamento = int(input("Qual será a condição do pagamento? (Digite o número correspondente)\n1. À Vista\n2. Parcelado em 2x\n3. Parcelado em 3x\n"))

if (parcelamento == 1):
    forma_pgto = int(input("Qual será a forma de pagamento? (Digite o número correspondente)\n1. Dinheiro\n2. Cheque\n3. Cartão de Crédito\n"))
    if (forma_pgto == 1):
        precodesconto = (preco * (100 - 10))/100
        print("O valor final a ser pago é de R$ ",precodesconto," à vista, no dinheiro.")
    elif (forma_pgto == 2):
        precodesconto = (preco * (100 - 10))/100
        print("O valor final a ser pago é de R$ ",precodesconto," à vista, no cheque.")
    elif (forma_pgto == 3):
        precodesconto = (preco * (100 - 15))/100
        print("O valor final a ser pago é de R$ ",precodesconto," à vista, no cartão de crédito.")
    else:
        print("Forma de pagamento inválida")

elif (parcelamento == 2):
    precodesconto = (preco)
    print("O valor final a ser pago é de R$ ",precodesconto," parcelado em 2x no cartão de crédito.")

elif (parcelamento == 3):
    precodesconto = preco * (100 + 10)/100
    print("O valor final a ser pago é de R$ ",precodesconto," parcelado em 3x, no cartão de crédito.")

else:
    print("Condição de pagamento inválido.")
