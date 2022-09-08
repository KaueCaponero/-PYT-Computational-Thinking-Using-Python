a1 = 1
an = 1
i = 1

for i in range(1,31,1):

    if (i <= 2):
        print(f"{i}. {an}")
        i = i + 1

    else:
        ax = a1 + an
        print(f"{i}. {ax}")
        a1 = an
        an = ax