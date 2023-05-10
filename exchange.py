from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exchange')
def exchange():
    return render_template('exchange.html')

@app.route('/exchange/update', methods=['POST'])
def get_exchange_rate():
    send_currency = request.json['send_currency']
    receive_currency = request.json['receive_currency']

    # получить курс обмена с помощью API
    exchange_rate = requests.get(f'https://api.exchangeratesapi.io/latest?base={send_currency}&symbols={receive_currency}').json()['rates'][receive_currency]

    return jsonify({ 'exchange_rate': exchange_rate })

@app.route('/exchange/confirm', methods=['POST'])
def confirm_exchange():
    send_currency = request.json['send_currency']
    receive_currency = request.json['receive_currency']
    send_amount = float(request.json['send_amount'])
    receive_amount = float(request.json['receive_amount'])
    exchange_rate = float(request.json['exchange_rate'])

    # осуществляем обмен
    # ...

    return jsonify({ 'message': 'Exchange complete.' })

if __name__ == '__main__':
    app.run(debug=True)

