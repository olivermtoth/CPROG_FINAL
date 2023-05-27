"""
Main application file.
Run as 'flask run' from the terminal
"""
from flask import Flask, render_template, request
import json
from stock import Stock
import os
from flask_apscheduler import APScheduler

# set configuration values
class Config:
    SCHEDULER_API_ENABLED = True


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

balance = 100_000.00

app = Flask(__name__)
app.config.from_object(Config())


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return render_template('index.html.jinja', balance=balance)
    else:
        print("Form submitted")
        try:
            stock = request.form.get("stock")
            s = Stock(stock)
            # data = s.make_json()
            return render_template("stock.html.jinja", stock=stock, balance=balance, price= s.current_price, data = s.reader.get_data_for_charts())
        except KeyError:
            print("Key Error raised, directing to the error page")
            return render_template("tickererror.html.jinja", balance=balance)