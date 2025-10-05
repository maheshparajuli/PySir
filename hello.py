from flask import Flask
from flask import request
from markupsafe import escape

app=Flask(__name__)



@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask") #URL bata name parameter ko value ley bhaneko ho
    return f"Hello, {escape(name)}!"

