from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exchange', methods=['GET', 'POST'])
def exchange():
    if request.method == 'POST':
        # Получаем данные из формы
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = request.form['amount']

        # Получаем текущий курс криптовалют с стороннего сервера
        url = f'https://api.cryptonator.com/api/ticker/{from_currency}-{to_currency}'
        response = requests.get(url).json()
        rate = response['ticker']['price']

        # Выполняем обмен
        total = float(amount) * float(rate)

        # Возвращаем результат обмена
        return jsonify({
            'status': 'success',
            'from_currency': from_currency,
            'to_currency': to_currency,
            'rate': rate,
            'amount': amount,
            'total': total
        })
    else:
        # Выводим форму для обмена криптовалют
        return render_template('exchange.html')

if __name__ == '__main__':
    app.run(debug=True)