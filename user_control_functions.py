from string import ascii_lowercase
from string import ascii_uppercase

def kucukHarf(kullaniciAdi):
    for harf in kullaniciAdi:
       for kontrolHarf in ascii_lowercase:
           if harf==kontrolHarf:
              return True
    return False

def buyukHarf(kullaniciAdi):
    for harf in kullaniciAdi:
        for kontrolHarf in ascii_uppercase:
            if harf==kontrolHarf:
                return True
    return False

def sayi(kullaniciAdi):
    sayiListe = ['0','1','2','3','4','5','6','7','8','9']
    for harf in kullaniciAdi:
        for kontrolHarf in sayiListe:
            if harf==kontrolHarf:
                return True
    return False


def karakter(kullaniciAdi):
    karakterListesi = ['*','-','_','/','\',"!",''','#','+','%','&','{','}','(',')','[',']',';',',',':','.','<','>','"']
    for harf in kullaniciAdi:
        for kontrolHarf in karakterListesi:
            if harf==kontrolHarf:
                return True
    return False

#Aşağıdakiler koda dönüştürülecektir#############################################
# def veritabaniKullaniciAdiEkleme(kullaniciAdi):
#     kullaniciAdiListe=['veritabanındaki kullanıcı adları']
#     for kontrolAd in kullaniciAdiListe:
#         if kullaniciAdi==kontrolAd:
#             return False
#     return True

# def veritabaniKullaniciAdiAktiflikKontrol(kullaniciAdi):
#     kullaniciAdiListe=['veritabanındaki kullanıcı adları']
#     for kontrolAd in kullaniciAdiListe:
#         if kullaniciAdi==kontrolAd:
#             if kontrolAdin_Aktiflik_Durumu == 1 :#Aktifmi?
#                 print('bu isimde aktif kullanıcı var')
#             else:
#                 print('bu isimde pasif kullanıcı var')
 #################################################################3       

def kontrol(kullaniciAdi):
    isKucuk=kucukHarf(kullaniciAdi)
    isBuyuk=buyukHarf(kullaniciAdi)
    isSayi=sayi(kullaniciAdi)
    isKarakter=karakter(kullaniciAdi)

    if len(kullaniciAdi)<16 and len(kullaniciAdi)>6:
        uzunluk = True
    else:
        uzunluk=False
    
    if isBuyuk==True  and isKucuk==True and uzunluk==True and isSayi==True :
        print('Kullanıcı adı formata uygundur')
    else:
        print('Kullanıcı adı seçim  şartları: en az 1 büyük harf, en az 1 küçük harf, en az 1 sayı ve uzunluğu 6 ile 16 arası olmalıdır.')


kullaniciAdi=input("Kullanıcı Adı giriniz: ")

kontrol(kullaniciAdi)