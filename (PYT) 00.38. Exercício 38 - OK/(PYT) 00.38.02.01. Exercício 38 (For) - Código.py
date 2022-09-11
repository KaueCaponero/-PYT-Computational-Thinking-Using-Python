a1 = 1
print(f"{a1} +")

for an in range(2,101,1):
    print (f"{an} +")
    an = an + 1

an = an - 1
sn = ((a1 + an) * an) / 2

print(f"Soma = {sn}")