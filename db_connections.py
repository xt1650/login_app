import sqlite3
def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}


con = sqlite3.connect("tutorial.db")
cur = con.cursor()
con.row_factory = dict_factory

# for row in con.execute("SELECT 1 AS a, 2 AS b"):
#     print(row)

cur.execute("CREATE TABLE IF NOT EXISTS user("
            "id integer primary key,"
            "username varchar(20) not null ,"
            "password varchar(255) not null,"
            "date timestamp default current_timestamp,"
            "state smallint default 0)")
#
# cur.execute("""
#     INSERT INTO user(username,password) VALUES
#         ('ahmet.turhan', '123456' ),
#         ('esra.aydin','1234es')
# """)
# res = cur.execute("SELECT * FROM user")
#
# data = res.fetchall()
# con.commit()
# print(data)




# print(data)
