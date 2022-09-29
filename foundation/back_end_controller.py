from db_controller import check, create_user, del_user, update_user, get_user_info


class Api:
    def __init__(self):
        check()

    def create_user(self):
        #! get user name and password hash
        create_user()

    def del_user(self):
        #! get user name and password hash
        #! use self.get_user_info() to check authenticate user
        del_user()

    def update_user(self):
        #! get user name password hash and relevant information to update user information in db
        #! use self.get_user_info() to check authenticate user
        update_user()

    def get_user_info(self):
        #! get user name and password hash
        get_user_info()

    def check_user_login(self):
        #! receive users passwords hash
        #! check if received hash maches with users passwords hash
        #! use self.get_user_info() to check authenticate user
        #! if so proceed (return True)
        #! else do not (return False)
        pass
