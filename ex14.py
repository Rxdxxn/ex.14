n = int(input('Dati numarul de coloane si randuri:\n'))
if 2 <= n <= 10:
    matrice = []
    for i in range(n):
        list = []
        for j in range(n):
            list.append(int(input(f'Dati element pe pozitia {i}:{j}: ')))
        matrice.append(list)
    for linie in matrice:
        print(linie)
    sp = []
    jp = []
    ss = []
    js = []
    ds = []
    dp = [matrice[i][i] for i in range(len(matrice))]
    print(f'Suma elementelor din diagonala principala este {sum(dp)}')
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if i + j == len(matrice) - 1:
                ds.append(matrice[i][j])
            if i < j:
                sp.append(matrice[i][j])
                jp.append(matrice[j][i])
            if i + j < len(matrice) - 1:
                ss.append(matrice[i][j])
            if i + j > len(matrice) - 1:
                js.append(matrice[i][j])
    print(f'Suma elementelor din diagonala secundara este {sum(ds)}')
    print(f'Suma elementelor din partea de sus a diagonalei principale este: {sum(sp)}')
    print(f'Suma elementelor din partea de jos a diagonalei principale este: {sum(jp)}')
    print(f'Suma elementelor din partea de sus a diagonalei secundare este: {sum(ss)}')
    print(f'Suma elementelor din partea de jos a diagonalei secundare este: {sum(js)}')
else:
    print('Dati un numar ed linii si coloane intre 2 si 10')