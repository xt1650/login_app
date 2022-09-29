from sqlite3 import connect
from os.path import abspath, dirname, join, exists

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


def check_user():
    conn, cursor = create_connection()
    #! check if user exists
    #! and return a boolean based on that information
    cursor.close()
    conn.close()


def create_user():
    conn, cursor = create_connection()
    # if not check_user():
    #     pass
    #! if user does not exist
    #! add user to the db
    #! with provided information
    conn.commit()
    cursor.close()
    conn.close()


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
