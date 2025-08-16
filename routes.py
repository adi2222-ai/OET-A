from flask import Flask

app = Flask(__name__)

@app.route("/")   # This is the root URL
def home():
    return "Hello Render!"  
