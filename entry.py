from flask import Flask,request,render_template
from markupsafe import escape


"""
def check():
    return 'Thik xa, info correct xa timro, tara website nei banya xaina'
def formi():
    return 'form nei banako xaina, kehi din ajhai lagxa'

app=Flask(__name__)

@app.route('/ja_jatha',methods=['GET','POST'])
def login():
    if request.method=='POST':
        return check()
    
    else:
        return formi()
    

#arko method ni xa hai, which is more cleaner, using @app.get and @app.post.
    
"""

app=Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

#so, i found out one thing that jinja is used for loading dynamic contents in webpages.

"""
Automatic escaping → protects you by showing raw HTML as text.

|safe or Markup() → tells Jinja2 “I know this is safe, please render it as real HTML.”


# Local context: Flask keeps the real request objects in a thread-local store, and the proxy automatically fetches the correct one.


"""
with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

"""  
with app.test_request_context('/hello', method='POST'):

This line simulates an HTTP request to your Flask app.

The request URL is /hello

The HTTP method is POST

So, Flask behaves as if a user sent a POST request to http://localhost/hello,
but it's only in memory — nothing is really sent.


Inside the with block

Within this block, you can access the request object, just like in a real route.

 assert request.path == '/hello'
assert request.method == 'POST'
are simply tests checking whether:

the simulated request's path is /hello

and the HTTP method is POST

If either of those conditions is false, the test will raise an AssertionError.

When the with block ends, the request context is automatically cleaned up.
Outside that block, request is no longer valid.

Thus, This code is used for testing or experimenting with Flask's
 request handling without starting a real server.
"""

""" with app.request_context(environ):
    assert request.method == 'POST'
    
    this is just another method of simulating the request.
    
    
    """