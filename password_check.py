# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 10:01:48 2022

@author: Administrator
"""
#Şifre Belirleme Kontrol:
#    -En az 8 karakter olacak
#    -En az 2 rakam içerecek
#    -En az 1 büyük harf içerecek
#    -En az 1 özel karakter içerecek(!,$,%,-,_,@)

def password_check(password):
    kharf, bharf, rakam, okarakter = 0, 0, 0, 0
    while True:
        if (len(password) >= 8):
            for char in password:
         
                # Küçük Harf Kontrolü
                if (char.islower()):
                    kharf+=1           
         
                # Büyük Harf Kontrolü
                if (char.isupper()):
                    bharf+=1           
         
                # Rakam Kontrolü
                if (char.isdigit()):
                    rakam+=1           
         
                # Özel Karakter Kontrolü
                if(char=='@'or char=='$' or char=='_' or char=='%' or char=='-'):
                    okarakter+=1          
        if (kharf>=1 and bharf>=1 and rakam>=2 and okarakter>=1 and kharf+bharf+rakam+okarakter==len(password)):
            print('Şifre oluşturuldu.')
            break
        else:
            password= password_check(str(input('-En az 8 karakter olacak\nEn az 2 rakam içerecek\nEn az 1 büyük harf içerecek\nEn az 1 küçük harf içerecek\nEn az 1 özel karakter içerecek(!,$,%,-,_,@)\n Lütfen şifre belirleyiniz: ')))
            break
password= password_check(str(input('-En az 8 karakter olacak\nEn az 2 rakam içerecek\nEn az 1 büyük harf içerecek\nEn az 1 küçük harf içerecek\nEn az 1 özel karakter içerecek(!,$,%,-,_,@)\n Lütfen şifre belirleyiniz: ')))

