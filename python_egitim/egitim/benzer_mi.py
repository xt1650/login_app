# bu egzersizde kullanicidan alinan iki cumlenin birbirleri ile benzer olup olmadigini kontrol edecegiz
# benzerlik kriterimiz cumlelerin puanlamalarinin birbirleriyle ayni olmasi olsun
# bu puanlamalar su sekilde yapilsin
# cumle icerisinde kullanilan her harfe sayisal bir deger verin ve bu degerleri bir sozluk objesinde tutun
# cumle icerisinde gecen her harf icin tek tek karsilik geldigi degerlerin toplamini bulun
# bu toplam cumlenin puani
# iki cumlenin puanlamalari esit ise bu cumleler benzerdir
def asaluret():
    asalListe=list()
    for sayi in range(1,700):
        asalmi=True
        for mod1 in range(2,sayi):
            if(sayi%mod1==0):
                asalmi=False
                break
        if asalmi==True:
            asalListe.append(sayi)
    return asalListe



puan_tablo={}

from itertools import count
from string import ascii_letters

alfabe=ascii_letters
asallar=asaluret()
print(asallar)


while True:
    i=0
    puan_tablo[alfabe[i]]=asallar[i]
    i+=1
    if(len(alfabe)==len(puan_tablo)):
        break


print(puan_tablo)
    

