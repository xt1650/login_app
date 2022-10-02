from db_controller import DB_Controller


class Api:
    def __init__(self, controller):
        self.db_controller = DB_Controller()
        self.controller = controller

    def console_log(self, message):
        print(message)

    def add_user(self, username, password_hash):

        current_url = self.controller.window.get_current_url()
        _tmp = ''
        flag = False
        for char in reversed(current_url):
            if not flag:
                if char == '/':
                    flag = True
            else:
                _tmp += char
        base_url = _tmp[::-1]

        #! i need to figure out how to take action in javascript
        #! based on res variable in this method
        #! or find a way to pass pywebview window here and take
        #! action in javascript based on res here somehow
        res = self.db_controller.add_user(username, str(password_hash))
        if res == 'success':
            self.controller.window.load_url(base_url + '/login')
        elif res == 'user_exists':
            self.controller.window.load_url(base_url + '/')
        elif res == 'integrity_error':
            self.controller.window.destroy()
            exit()
        else:
            self.controller.window.destroy()
            exit()

    def login(self, username, password_hash):

        current_url = self.controller.window.get_current_url()
        _tmp = ''
        flag = False
        for char in reversed(current_url):
            if not flag:
                if char == '/':
                    flag = True
            else:
                _tmp += char
        base_url = _tmp[::-1]

        #! there is a lot can go wrong
        db_user_id, db_username, db_password_hash, db_creaetion_date = self.db_controller.get_user_info(
            username)
        if str(password_hash) == db_password_hash:
            #! password check is successfull
            #! therefore redirect user to change_password page
            self.controller.window.load_url(
                base_url + f'/change_password/{username}')
        else:
            #! password check is unsuccessfull
            self.controller.window.load_url(base_url)
            print('wrong password')

    def change_password(self, username, old_password_hash, new_password_hash):
        current_url = self.controller.window.get_current_url()

        _tmp = ''
        flag1 = False
        flag2 = False
        for char in reversed(current_url):
            if not flag1 or not flag2:
                if char == '/':
                    if flag1:
                        flag2 = True
                    else:
                        flag1 = True

            else:
                _tmp += char
        base_url = _tmp[::-1]

        #! check if user exists
        #! if it does check its passwords are matching
        #! if passwords do match than update its password with new_password_hash
        #! than send user to login page
        #! if passwords do not match tho send user back to landing page
        #! if user does not exist than send user to /sing_up
        res = self.db_controller.change_password(
            username, str(old_password_hash), str(new_password_hash))
        if res == 'success':
            self.controller.window.load_url(base_url + '/login')
        elif res == 'wrong_password':
            pass
        elif res == 'user_not_exits':
            pass
        else:
            pass
