from db_controller import DB_Controller


class Api:
    def __init__(self):
        self.db_controller = DB_Controller()
        # self.db_controller.check_db()
        pass

    def create_user(self):
        #! get user name and password hash
        # self.db_controller.create_user()
        pass

    def del_user(self):
        #! get user name and password hash
        #! use self.get_user_info() to check authenticate user
        # self.db_controller.del_user()
        pass

    def update_user(self):
        #! get user name password hash and relevant information to update user information in db
        #! use self.get_user_info() to check authenticate user
        # self.db_controller.update_user()
        pass

    def get_user_info(self):
        #! get user name and password hash
        # self.db_controller.get_user_info()
        pass

    def check_user_login(self):
        #! receive users passwords hash
        #! check if received hash maches with users passwords hash
        #! use self.get_user_info() to check authenticate user
        #! if so proceed (return True)
        #! else do not (return False)
        pass
