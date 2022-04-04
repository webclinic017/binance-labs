import config
import csv

from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

# prices = client.get_all_tickers()
# for price in prices:
#     print(price)

""" last_candles = client.get_klines(
    symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)
csvfile = open('15minutes.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')
for candlestick in last_candles:
    candlestick_writer.writerow(candlestick)
csvfile.close()

history_candles = client.get_historical_klines(
    'BTCUSDT', Client.KLINE_INTERVAL_5MINUTE, '1 Apr, 2012', '1 Apr, 2022')
csvfile = open('2012-2022.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')
for candlestick in history_candles:
    candlestick_writer.writerow(candlestick)
csvfile.close() """

history_candles = client.get_historical_klines(
    'BTCUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan, 2022', '4 Apr, 2022')
csvfile = open('daily-2022.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')
for candlestick in history_candles:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)
csvfile.close()
