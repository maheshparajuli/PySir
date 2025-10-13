from flask import Flask,render_template,session,url_for,redirect,request

app=Flask(__name__)

app.secret_key='kxamm'
@app.route('/')
def index():
    if 'username' in session:
        return f'logged in as {session['username']}'
    return 'you are not logged in'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        session['username']
        

"""
just a look how session look like:
{
  "sessionId": "8f3a1d9d-2b4c-4e7a-9a1b-5c8f0e2d6a1f",
  "userId": "user_12345",
  "isAuthenticated": true,
  "roles": ["student"],
  "permissions": ["read:projects","create:notes"],
  "createdAt": "2025-10-13T14:05:22.000Z",
  "expiresAt": "2025-10-14T14:05:22.000Z",
  "lastActivity": "2025-10-13T20:32:10.000Z",
  "device": "Chrome 141 on Windows 10",
  "ip": "203.0.113.45",
  "csrfToken": "a6f4b2c9",
  "refreshTokenId": "rt_98765",
  "sessionData": {
    "theme": "dark",
    "lastOpenProject": "GraphColoringMini",
    "preferredSemesterView": "Sem 4"
  },
  "authMethod": "password",
  "locale": "ne-NP"
}




"""
