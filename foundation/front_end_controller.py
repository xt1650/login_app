from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('landing.html')


@app.route('/login')
def user_info():
    return render_template('login.html')


@app.route('/sign_up')
def user_info():
    return render_template('sign_up.html')


@app.route('/change_password')
def user_info():
    return render_template('change_password.html')


if __name__ == '__main__':
    app.run(debug=True)
