from sqlite3 import connect
from os.path import abspath, dirname, join, exists


class DB_Controller:
    def __init__(self, db_name='login_app.db'):
        self.path = dirname(abspath(__file__))
        self.db_path = join(self.path, db_name)
        self.check_db()
        self.conn, self.cursor = None, None
        self.create_connection()

    def check_db(self):
        if not exists(self.db_path):
            conn = connect(self.db_path)
            conn.close()

    def create_connection(self):
        self.conn = connect(self.db_path)
        self.cursor = self.conn.cursor()

    def destroy_connection(self):
        #! destroys self.conn and self.cursor
        pass

    def commit_and_destroy_connection(self):
        #! first commits on self.conn
        #! then referres to self.destroy_connection
        pass

    def check_user(self):
        #! check if user exists
        #! and return a boolean based on that information
        pass

    def create_user(self):
        # if not self.check_user():
        #     pass
        #! if user does not exist
        #! add user to the db
        #! with provided information
        # self.conn.commit()
        pass

    def del_user(self):
        #! delete user
        # conn.commit()
        pass

    def update_user(self):
        #! update user information
        # conn.commit()
        pass

    def get_user_info(self):
        # if check_user():
        #     pass
        #! get user information if user exists
        pass
