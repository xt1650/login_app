import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS user("
            "id integer primary key,"
            "username varchar(20)  null ,"
            "email varchar(200) unique not null ,"
            "password varchar(255) not null,"
            "date timestamp default current_timestamp,"
            "state smallint default 0)")

# cur.execute("""
#     INSERT INTO user(username,email,password) VALUES
#         ('ahmet.turhan','ahmet.turhan@diyanet.gov.tr','123456' ),
#         ('esra.aydin','esra.aydin@diyanet.gov.tr','1234es')
# """)
#
# res = cur.execute("SELECT * FROM user")
# data = res.fetchall()
# con.commit()
# print(data)




# print(data)
