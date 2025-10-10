from flask import Flask,request,render_template

app=Flask(__name__)

from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'kxa' 


USERS = {
    'mahesh': '1234sova@#',
    'admin': 'admin123'
}


def valid_login(username, password):
    """Return True if username and password match the database."""
    # Check if username exists and password is correct
    if username in USERS and USERS[username] == password:
        return True
    return False

#Function to log the user in 
def log_the_user_in(username):
    """Simulate logging the user in."""
    #store username in session (Flask’s way to remember users)
    session['username'] = username
    #redirect to a welcome page
    return redirect(url_for('welcome'))

# Login route
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

#A simple page after login
@app.route('/welcome')
def welcome():
    if 'username' in session:
        return f"Welcome, {session['username']}!"
    return redirect(url_for('login'))
