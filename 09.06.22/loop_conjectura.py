n = 1

while 1:
    print(f"N = {n}")
    sucessor = n
    while sucessor != 1:
        if sucessor % 2 == 0:
            sucessor = sucessor / 2
        else:
            sucessor = (3 * sucessor) + 1
        print(sucessor)
    n += 1