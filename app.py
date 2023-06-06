"""
Main application file.
Run as 'Python3 app.py'
"""
from flask import Flask, render_template, request
import json
from stock import Stock
import os
from flask_apscheduler import APScheduler

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
BASKET = { 'meta':Stock('meta'),
           'aapl':Stock('aapl'),
            'amzn':Stock('amzn'), 
            'msft':Stock('msft'),
            'nvda':Stock('nvda')}
BALANCE = 100_000.00


# set configuration 
class Config:
    SCHEDULER_API_ENABLED = True

app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()

@scheduler.task('cron', id='trade', hour=21, minute=00, day_of_week='mon-fri')
def trade():
    """
    Make predictions and trades @ 17:00 EST (21:00 UTC)
    """
    print('Scheduling works')

scheduler.init_app(app)
scheduler.start()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html.jinja', balance=BALANCE)
    elif request.method == "POST":
        print("Form submitted")
        try:
            ticker = request.form.get("stock")
            if ticker.lower() not in BASKET.keys():
                raise KeyError
            else:
                BASKET[ticker].get_data()
                return render_template("stock.html.jinja", ticker=ticker, balance=BALANCE, price=BASKET[ticker].current_price, data = BASKET[ticker].chart_data)
        except KeyError:
            print("Key Error raised, directing to the error page")
            return render_template("tickererror.html.jinja", balance=BALANCE)
        

@app.route('/preformance')
def performance():
    return render_template('performance.html.jinja', balance = BALANCE)

if __name__ == "__main__":
    app.run(debug=True, port=5000)