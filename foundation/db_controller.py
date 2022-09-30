from sqlite3 import connect
from os.path import abspath, dirname, join, exists

print("deneme")

PATH = dirname(abspath(__file__))
DB_PATH = join(PATH, 'login_app.db')


def check():
    if not exists(DB_PATH):
        conn = connect('login_app.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS user("
                    "id integer primary key,"
                    "email varchar(200) unique not null ,"
                    "password varchar(255) not null,"
                    "date timestamp default current_timestamp,"
                    "state smallint default 0)")
        conn.commit()
        cursor.close()
        conn.close()


def create_connection():
    print('baglanti')
    conn = connect('login_app.db')
    cursor = conn.cursor()
    return (conn, cursor)


def check_user(email):

    print(email)
    conn, cursor = create_connection()
    #! check if user exists
    #! and return a boolean based on that information
    rs = cursor.execute('SELECT * FROM user where email=:params',dict(params=email))
    data = rs.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    
    if data is None:
        return  {'user':False,'data':None,'info':'Kullanici bulunamadi'}
    else:
        return {'user':True,'data':data}

def create_user(email,params):
    print('create user')
    conn, cursor = create_connection()

    # if not check_user():
    #     pass
    #! if user does not exist
    #! add user to the db
    #! with provided information
    rs = check_user(email)
    print(rs)
    if not rs['user']: #Kullanici yok ise
        cursor.execute("insert into user(email,password) values(:email,:password)",
                       dict(email=params['email'],password=params['password']))
        conn.commit()
        cursor.close()
        conn.close()
        return {'user':'created','status':True}
    else:
        return {'status':False, 'info':'Kullanici mevcuttur.Kayit yapilamaz'}


def del_user(u_id):
    conn, cursor = create_connection()
    #! delete user
    effected_rows = cursor.execute("delete from user where id=:user_id",dict(user_id=u_id)).rowcount
    conn.commit()
    cursor.close()
    conn.close()
    if effected_rows > 0:
        return {'action':True,'effected':effected_rows}
    else:
        return  {'action':False,'effected':0}

def update_user(id,newEmail,newPassword):
    conn, cursor = create_connection()
    #! update user information

    cursor.execute("update user "
                    "set password=:newPass,"
                    "set email=:newEmail where id=:id", dict(id=id,newPass=newPassword,newEmail=newEmail))

    conn.commit()
    cursor.close()
    conn.close()
    return {'action':True}


def get_user_info(email):
    conn, cursor = create_connection()
    # if check_user():
    #     pass
    #! get user information if user exists
    check_user(email)


