p1 = float(input("Preencha o valor do 1º Produto: "))
p2 = float(input("Preencha o valor do 2º Produto: "))
p3 = float(input("Preencha o valor do 3º Produto: "))
p4 = float(input("Preencha o valor do 4º Produto: "))
p5 = float(input("Preencha o valor do 5º Produto: "))

valorpago = float(input("Preencha o valor pago: "))

troco = valorpago - (p1 + p2 + p3 + p4 + p5)

print("O troco é de R$", troco)