# kullanicidan sayisal bir deger alin bu degerin sayisal olmadigi durumda kullaniciyi uyarip kullanicidan 
# bu degeri tekrar isteyin
# kullanicidan yapilacak islemi alin ayni sekilde gecersiz bir islem girildiginde kullaniciyi uyarip
# yeniden bir islem girmesini talep edin
# yine kullanicidan sayisal bir deger alin ilk degerde oldugu gibi kontrollerinizi saglayin
# ilgili islemi gerceklestirin ve sonucu ekrana yazdirin

print("------")
islemler=["+","-","*","/"]
islem=""
deger1=0
deger2=0
sonuc=0
while not deger1 :
    try:
        deger1=int(input("Sayi giriniz >> "))
    except:
        print("Sayi değeri giriniz")

while islem not in islemler:
    
    islem= input("işlem tipi giriniz >> ")

while not deger2 :
    try:
        deger2=int(input("Sayi giriniz >> "))
    except:
        print("Sayi değeri giriniz")
    
if(islem=="+"):
    sonuc=deger1+deger2
elif(islem=="-"):
    sonuc=deger1-deger2
elif(islem=="*"):
    sonuc=deger1*deger2
elif(islem=="/"):
    sonuc=deger1/deger2


print("islem sonucu")
print(sonuc)
