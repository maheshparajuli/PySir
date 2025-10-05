from flask import Flask
from flask import request
from markupsafe import escape

app=Flask(__name__)



@app.route("/hello")
def hello():
    """request.args.get("name", "Flask") means:

Get the value of name from the URL query.
If it doesnt exist, use 'Flask' as the default."""
    name = request.args.get("name", "Flask") #URL bata name parameter ko value ley bhaneko ho
    return f"Hello, {escape(name)}!"

"""
request in flask: the request object is used to access data sent 
by the client (browser, app, etc.) to the server.
1. request.args: Access query parameters (from URL, e.g., ?name=Mahesh)

markupsafe: Flask imports escape from markupsafe internally.
So you can use escape() in Flask without installing markupsafe separately
 (because Flask already installs it as a dependency).
 
"""
