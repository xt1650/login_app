from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login():
    #! test for users password
    #! if its true send user to /info/<user_name>
    #! if user not found send user to /create_user
    return render_template('login.html')


@app.route('/info/<user_name>')
def user_info(user_name):
    #! render user information
    return render_template('user_info.html')


@app.route('/create_user')
def create_user():
    #! a basic user creation page
    return render_template('create_user.html')


if __name__ == '__main__':
    app.run(debug=True)
