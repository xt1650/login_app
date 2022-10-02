from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('landing.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/sign_up')
def sigh_up():
    return render_template('sign_up.html')


@app.route('/change_password/<username>')
def change_password(username):
    return render_template('change_password.html')


if __name__ == '__main__':
    app.run(debug=True)
