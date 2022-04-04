from distutils.command.clean import clean
from flask import Flask, render_template, request, flash, redirect, jsonify
import config
import csv
from binance.client import Client

app = Flask(__name__)
app.secret_key = b'change-this-secret_key'

client = Client(config.API_KEY, config.API_SECRET)


@app.route('/')
def index():
    title = 'CoinView'

    account = client.get_account()
    balances = account['balances']
    filtered_balances = list(filter(lambda d: d['asset'] in [
                             'BTC', 'USDT', 'LTC', 'ETH'], balances))

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']
    filtered_symbols = list(filter(lambda d: d['symbol'] in [
        'BTCUSDT', 'LTCUSDT', 'ETHUSDT'], symbols))

    return render_template(
        'index.jinja',
        title=title,
        my_balances=filtered_balances,
        symbols=filtered_symbols
    )


@app.route('/buy', methods=['POST'])
def buy():
    try:
        order = client.create_order(
            symbol=request.form['symbol'],
            side=client.SIDE_BUY,
            type=client.ORDER_TYPE_MARKET,
            quantity=request.form['quantity']
        )
    except Exception as e:
        flash(e.message, 'error')

    return redirect('/')


@app.route('/sell')
def sell():
    return 'sell'


@app.route('/settings')
def settings():
    return 'settings'


@app.route('/history')
def history():
    candlesticks = client.get_historical_klines(
        'BTCUSDT',
        Client.KLINE_INTERVAL_15MINUTE,
        '01 Apr 2022',
        '03 Apr 2022'
    )

    processed_candlesticks = []

    for data in candlesticks:
        candlestick = {
            'time': data[0] / 1000,
            'open': data[1],
            'high': data[2],
            'low': data[3],
            'close': data[4],
        }

        processed_candlesticks.append(candlestick)

    response = jsonify(processed_candlesticks)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
