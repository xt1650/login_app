from db_controller import DB_Controller


class Api:
    def __init__(self):
        self.db_controller = DB_Controller()

    def console_log(self, message):
        print(message)

    def add_user(self, username, password_hash):
        res = self.db_controller.add_user(username, str(password_hash))
        return {'res': res}
