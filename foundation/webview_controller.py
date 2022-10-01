from webview import create_window, start
from front_end_controller import app
from back_end_controller import Api


#! everything comes together in here

class Controller:
    def __init__(self):
        self.js_api = None
        self.window = None
        self.window_title = 'login_app'

    def run(self):
        self.js_api = Api()
        self.window = create_window(self.window_title)
        start()


if __name__ == '__main__':
    api = Api()
    create_window('login app', app, js_api=api)
    start()
