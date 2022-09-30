import db_connections

rs = db_connections.cur.execute("SELECT * FROM user where email='ahmet1.turhan@diyanet.gov.tr'")
row = rs.fetchone()
db_connections.con.commit()
print (row)
def userAuthControl(email, password):
    rs = db_connections.cur.execute("SELECT * FROM user where email=:params", dict(params=email))
    row = rs.fetchone()
    db_connections.con.commit()
    print(row)
    if row is  None:
        return {'auth': False, 'code': 'Kullanici adi bulunamadi.'}
    dbHashPassword = row[2]
    if len(password) == len(dbHashPassword):  # hash uzunluklar? e?it mi
        i = 0
        for char in password:
            if char == dbHashPassword[i]:
                i += 1
                continue
            else:
                return {'auth': False, 'code': 'Sifre Dogrulama Basarisiz'}

        return {'auth': True}
    else:
        return {'auth': False, 'code': 'Sifre Uzunluklari esit degil'}





# def userSave()
#
#
print(userAuthControl('ahmet1.turhan@diyanet.gov.tr', "123456"))
