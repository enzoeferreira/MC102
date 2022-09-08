n = 1
nMax = 0
passosMax = 0

while 1:
    print(f"N = {n}")
    sucessor = n
    passos = 0
    
    while sucessor != 1:
        if sucessor % 2 == 0:
            sucessor = sucessor / 2
            passos += 1
        else:
            sucessor = (3 * sucessor) + 1
            passos += 1
        print(sucessor)
    
    if passos >= passosMax:
        passosMax = passos
        nMax = n
    print(f"Maior N = {nMax}, Maior passos = {passosMax}")
    
    n += 1