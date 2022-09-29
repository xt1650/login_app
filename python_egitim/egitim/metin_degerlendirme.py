# kullanicidan bir metin alin
# bu metin icerisinde ' ' (bosluk) haric her karakterin kac kez gectigini analiz edin
# ve bu analizin sonucunu ekrana yazin

from string import ascii_lowercase


metin=input('metin giriniz ')

#alfabe=ascii_lowercase
#print(alfabe)
#sozluk={}
#for karakter in alfabe:
#    adet=metin.count(karakter)
#    sozluk[karakter]=adet

#print(sozluk)

liste=list()

for harf in metin:
    if(harf!=" "):
        print(harf + "=" + str(metin.count(harf)))
        if harf not in liste:
            liste.append(harf)
       


            
    

