"""
Main application file.
Run as 'flask run' from the terminal
"""
from flask import Flask, render_template, request
import sqlite3 as sql
from stock import Stock

balance = 100_000

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return render_template('index.html', balance=balance)
    else:
        print("Form submitted")
        stock = request.form.get("stock")
        s = Stock(stock)
        data = s.make_json()
        return render_template("stock.html", stock=stock, data=data, balance=balance, price= s.current_price)