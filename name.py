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
        error = 'Invalid username/password'
    return render_template('login.html', error=error)

#route after login successful
@app.route('/welcome')
def welcome():
    if 'username' in session:
        return f"Welcome, {session['username']}!"
    return redirect(url_for('login'))

"""
some info on session instance ::

Flask's session is instance of a class called SecureCookieSession.
It behaves like a dictionary ({ key: value }).
Also, request.form is a kind of dictionary to understand for now.

Q. seems like secret key is not used here?
Ans: BUt what happens here is that Flask does these things internally. It stores session on client side in browser cookie,
and to keep it secure it have to sign in into that cokkie(cryptography seal)

Learn about 400 error or key error.
"""
