a = float(input("Digite o valor da aceleração (m/s): "))
v0 = float(input("Digite o valor da velocidade inicial (m/s): "))
t = float(input("Digite o tempo do percurso (s): "))

v = v0 + (a * t)

if (v <= 40):
    print("Veículo muito lento.")

elif (v > 40) and (v <= 60):
    print("Velocidade permitida.")

elif (v > 60) and (v <= 80):
    print("Velocidade de cruzeiro.")

elif (v > 80) and (v <= 120):
    print("Veículo rápido.")

else:
    print("Veículo muito rápido.")