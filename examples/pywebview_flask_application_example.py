from webview import create_window, start
from flask import Flask, jsonify, render_template

server = Flask(__name__)


class Api:
    def __init__(self) -> None:
        pass

    def test(self, a):
        print(a)

    def print_post(self, res):
        print(res)


@server.route('/')
def index():
    return render_template('index.html')


@server.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    api = Api()
    create_window('login application', server, js_api=api)
    start()
    # server.run(debug=True)
