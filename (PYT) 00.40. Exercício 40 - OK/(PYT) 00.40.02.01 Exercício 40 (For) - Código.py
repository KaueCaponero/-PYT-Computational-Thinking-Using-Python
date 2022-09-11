from re import A

a0 = 1
a1 = 1
an = 1
indice = 1

for i in range(1,21,1):

    if (indice <= 3):
        print(f"{indice}. {an}")
        indice = indice + 1

    else:
        ax = a0 + a1 + an
        print(f"{indice}. {ax}")
        a0 = a1
        a1 = an
        an = ax
        indice = indice + 1
