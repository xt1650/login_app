import db_connections


## Kullanıcı adı ve şifre kontrolünü sağlar
## Kullanıcı doğrulama işlemi gerçekleşirse dict('auth':True) döner
## doğrulama başarısız ise dict('auth':False,'error':'Hata gerekçisi)
def userAuthControl(username, password):
    rs = db_connections.cur.execute("SELECT * FROM user where username=:params", dict(params=username))
    row = rs.fetchone()
    db_connections.con.commit()
    if row is None:
        return {'auth': False, 'code': 'Kullanıcı adı bulunamadı'}
    else:
        dbHashPassword = row[2]
        if len(password) == len(dbHashPassword):  # hash uuzunlukları eşit mi
            i = 0
            for char in password:
                if char == dbHashPassword[i]:
                    i += 1
                    continue
                else:
                    return {'auth': False, 'code': 'Şifre Doğrulama Başarısız'}

            return {'auth': True}
        else:
            return {'auth': False, 'code': 'Şifre Uzunlukları eşit değil'}





# def userSave()
#
#
# print(userAuthControl('esra.aydin', "1234es"))
