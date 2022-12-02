# def suma()


with open("input1.txt") as plik:
    dane = plik.readlines()
    for i in range(len(dane)):
        dane[i] = dane[i].rstrip()
    print(dane)

    # zadanie 1
    skrzaty = []
    k = 0
    skrzat = 0
    for i in range(len(dane)):
        if dane[i] != '':
            skrzat += int(dane[i])
        else:
            skrzaty.append(skrzat)
            skrzat = 0
    print(skrzaty)
    # print(len(skrzaty))
    # print(dane.count(''))
    # print(max(skrzaty))
    # zadanie 2
    skrzaty.sort()
    print(sum(skrzaty[-3:]))
