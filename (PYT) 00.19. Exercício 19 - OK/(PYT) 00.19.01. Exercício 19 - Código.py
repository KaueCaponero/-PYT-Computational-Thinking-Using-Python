p1 = float(input("Digite sua nota da primeira avaliação: "))
p2 = float(input("Digite sua nota da segunda avaliação: "))

mf = ((p1 + (2 * p2)) / 3)

if mf >= 5:
    print("Aprovado")
else:
    print("Reprovado")