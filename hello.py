from flask import Flask
from flask import request
from markupsafe import escape

app=Flask(__name__)


@app.route('/user/<username>')
def show_user_profile(username):
    return f'user {escape(username)}'
