from sqlite3 import connect, IntegrityError
from os.path import abspath, dirname, join, exists
from time import sleep
from random import random


class DB_Controller:
    def __init__(self, db_name='login_app.db'):
        self.path = dirname(abspath(__file__))
        self.db_path = join(self.path, db_name)
        self.check_db()
        self.conn, self.cursor = None, None
        self.create_connection()

    def check_db(self):
        #! this is only for sqlite db's
        if not exists(self.db_path):
            conn = connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                create table user(id integer primary key, username varchar(20) unique not null,
                password varchar(255) not null,
                date timestamp default current_timestamp);
            ''')
            conn.commit()
            cursor.close()
            conn.close()

    def create_connection(self):
        self.conn = connect(self.db_path)
        self.cursor = self.conn.cursor()

    def destroy_connection(self):
        #! destroys self.conn and self.cursor
        self.cursor.close()
        self.conn.close()

    def get_user_info(self, username):
        #! return user information if user exists
        if self.check_user(username):
            #! therefore user exists gather its information and return it back
            query_result = self.cursor.execute('''
                SELECT * FROM user where username=:params
            ''', dict(params=username))
            return query_result.fetchone()
        else:
            return None

    def check_user(self, username):
        #! check if user exists by its username
        #! and return a boolean based on that information
        #! if user exits return True
        #! if user does not exist return False
        self.__init__()
        query_result = self.cursor.execute('''
            SELECT * FROM user where username=:params
        ''', dict(params=username))

        return not query_result.fetchone() is None

    def add_user(self, username, password_hash):
        #! if user does not exist
        #! add user to the db
        #! with provided information
        if not self.check_user(username):
            #! then user does not exist
            #! create the user with provided information
            try:
                self.cursor.execute('''
                    insert into user(username, password) values(:username,:password)
                ''', dict(username=username, password=password_hash))
                self.conn.commit()
                return True
            except IntegrityError as err:
                #! at this point there is a problem with the integrity of db most probably username constrain is not unique
                #! code should never reach here with the self.check_user
                print(f'an integrity error occured as follows >>\n{err}')
                return False
        else:
            #! user already exists take action accordingly
            print('user already exists in the db')
            return False

    def del_user(self, username, password_hash):
        #! check if user exists
        #! if not exists there is nothing to delete
        #! if user exits check if users password hash matches with the on in the db
        #! if password hash is not matching with the one in the db
        #! then do not remove the user
        #! if password hash matches with the on in the db
        #! then remove user from db

        if self.check_user(username):
            #! check if password hashes match
            db_id, db_username, db_password_hash, db_date = self.get_user_info(
                username)
            #! here sleep a random amount of milliseconds to prevent time forcing password cracking
            sleep(random())
            if password_hash == db_password_hash:
                #! passwords match
                #! therefore delete user
                self.cursor.execute(
                    "delete from user where id=:user_id", dict(user_id=db_id))
                self.conn.commit()
            else:
                #! user passwords do not match do not take action
                print('user password is not right')
        else:
            #! then user does not exist therefore there is nothing to remove from the db
            print('user does not exists in the db')

    def change_password(self, username, password_hash, new_password_hash):
        #! check for the existance of the user in the db
        #! if user exists check for if current password hashes matches
        #! if hashes match therefore change password hash in the db with the new_password_hash for the user

        if self.check_user(username):
            #! check if password hashes match
            db_id, db_username, db_password_hash, db_date = self.get_user_info(
                username)
            #! here sleep a random amount of milliseconds to prevent time forcing password cracking
            sleep(random())
            if password_hash == db_password_hash:
                #! passwords match
                #! therefore update users passwords hash with the new one
                self.cursor.execute(
                    "update user set password=:new_password_hash where id=:id", dict(new_password_hash=new_password_hash, id=db_id))
                self.conn.commit()
            else:
                #! user passwords do not match do not take action
                print('user password is not right')
        else:
            #! then user does not exist therefore there is nothing to remove from the db
            print('user does not exists in the db')


if __name__ == '__main__':
    db_controller = DB_Controller()
    db_controller.change_password('flouda', 'Resu123!', 'resu')
    db_controller.destroy_connection()
