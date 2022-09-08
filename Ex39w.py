a1 = 1
an = 1
i = 1

while (i <= 30):

    while (i <= 2):
        print(f"{i}. {an}")
        i = i + 1

    ax = a1 + an
    print(f"{i}. {ax}")
    a1 = an
    an = ax
    i = i + 1