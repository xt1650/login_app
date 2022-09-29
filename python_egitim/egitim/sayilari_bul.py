# kullanicidan bir metin alin
# bu metni ' ' (bosluk) karakterlerinden ayirin ve bu sayede sozcuklere ayirin
# ayirdiginiz sozcukler icerisinde sayi olup olmadiginin kontrolunu gerceklestirin
# buldugunuz her sayiyi ilgili numeric literal tipine cevirin ve saklayin
# buldugunuz sayilari ve sayilar ciktiktan sonra geriye kalan metni ekrana yazdirin

yazi=input('yazi giriniz ')

liste=list()
yazi_liste=list()
for sayi in yazi:
    try:
        sayi_eklenecek=int(sayi)
        liste.append(sayi_eklenecek)
    except ValueError:
        yazi_liste.append(sayi)
        continue

print(liste)
print(yazi_liste)


ornekTuple=(1)
print(ornekTuple)
