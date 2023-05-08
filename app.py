"""
Main application file.
Run as 'flask run' from the terminal
"""
from flask import Flask, render_template
import sqlite3 as sql


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
