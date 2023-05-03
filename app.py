"""
Main application file.
Run as 'flask run' from the terminal
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
