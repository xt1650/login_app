from sqlite3 import connect
from os.path import abspath, dirname, join, exists

print("deneme")

PATH = dirname(abspath(__file__))
DB_PATH = join(PATH, 'login_app.db')


def check():
    if not exists(DB_PATH):
        conn = connect('login_app.db')
        conn.close()


def create_connection():
    conn = connect('login_app.db')
    cursor = conn.cursor()
    return (conn, cursor)


def check_user(email):
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
    conn, cursor = create_connection()
    # if not check_user():
    #     pass
    #! if user does not exist
    #! add user to the db
    #! with provided information
    rs = check_user(email)
    if not rs['user']: #Kullanici yok ise
        cursor.execute("insert into user(email,password) values(:email,:password)",
                       dict(email=params['email'],password=params['password']))
        conn.commit()
        cursor.close()
        conn.close()
        return {'user':'created','status':True}
    else:
        return {'status':False, 'info':'Kullanici mevcuttur.Kayit yapilamaz'}


def del_user():
    conn, cursor = create_connection()
    #! delete user
    conn.commit()
    cursor.close()
    conn.close()


def update_user():
    conn, cursor = create_connection()
    #! update user information
    conn.commit()
    cursor.close()
    conn.close()


def get_user_info():
    conn, cursor = create_connection()
    # if check_user():
    #     pass
    #! get user information if user exists
    cursor.close()
    conn.close()
