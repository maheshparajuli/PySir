from flask import Flask,request,render_template,session,url_for,abort,redirect,render_template_string,make_response
# from markupsafe import escape

""" 
Redirect and errors:

use url_for wrapped up with redirect to redirect user to another page or endpoint.
And use abort to abort request made by client early with error code.

abort() is used when you want to stop processing a request and send a specific
HTTP error code back to the client.
"""


app = Flask(__name__)

# A pretend database of valid usernames
valid_users = ['mahesh', 'biplav','motey']

@app.route('/')
def home():
    return redirect(url_for('login'))  # Redirect to login page

@app.route('/login')
def login():
    username = request.args.get('user')
    
    if not username:
        return '<p>Please provide ?user=yourname in URL</p>'
    
    elif username not in valid_users:
        abort(401)
    
    # If user is valid, go to the profile page
    else:
        return redirect(url_for('profile', username=username))

@app.route('/profile/<username>')
def profile(username):
    return render_template_string("""
        <h2>Welcome, {{ name }}!</h2>
        <p>You are successfully logged in.</p>
    """, name=username)

@app.errorhandler(401)
def error_fu(error):
    rr=make_response(render_template('aftererr.html'), 401)
    rr.headers['do']='lekhnath'
    return rr


if __name__ == '__main__':
    app.run(debug=True)

# .\vir_env\Scripts\Activate

"""
About Responses:
make_response(): for customization

jsonify(*args,**kargs): useful method 

serialization: Serialization means converting complex data (like Python objects) into a
 format that can be easily stored, transmitted, or shared — most commonly into JSON.


"""
