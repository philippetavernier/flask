from flask import Flask, url_for
from markupsafe import escape
from flask import request

app = Flask(__name__)
@app.route('/')
def index():
    return 'index'

# @app.route('/login')
# def login():
#     return 'login'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
