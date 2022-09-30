from webview import create_window, start
from front_end_controller import app
from back_end_controller import Api

#! everything comes together in here
#! and this script will be used as the
#! entry point for the application

if __name__ == '__main__':
    api = Api()
    create_window('login app', app, js_api=api)
    start()
