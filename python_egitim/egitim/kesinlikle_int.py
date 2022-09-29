from itertools import count


def asaluret():
    asalListe=list()
    for sayi in range(1,200):
        asalmi=True
        for mod1 in range(2,sayi):
            if(sayi%mod1==0):
                asalmi=False
                break
        if asalmi==True:
            asalListe.append(sayi)
    return asalListe

print(count(asaluret()))
