from flask import Flask, render_template, request, redirect
import json
from datetime import datetime

app = Flask(__name__)

DATA_FILE = 'data.json'

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    curry = request.form.get('curry')
    role = request.form.get('role')
    price = float(request.form.get('price', 0))
    paid = True if request.form.get('paid') == 'on' else False
    date = datetime.now().strftime('%Y-%m-%d')

    data = load_data()
    if date not in data:
        data[date] = {}

    data[date][name] = {
        "curry": curry,
        "role": role,
        "price": price,
        "paid": paid
    }
    save_data(data)

    if role == "taker":
        return redirect("/taker")
    else:
        return redirect("/thanks")

@app.route('/thanks')
def thanks():
    return render_template("thanks.html")


@app.route('/taker')
def taker():
    data = load_data()
    today = datetime.now().strftime('%Y-%m-%d')
    today_data = data.get(today, {})
    return render_template('taker.html', curry_data=today_data)

# @app.route('/clear', methods=['POST'])
# def clear():
#     data = load_data()
#     today = datetime.now().strftime('%Y-%m-%d')
#     if today in data:
#         del data[today]
#         save_data(data)
#     return redirect('/taker')

from waitress import serve

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)

