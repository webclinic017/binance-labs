https://github.com/binance/binance-spot-api-docs
https://www.tradingview.com/lightweight-charts
https://github.com/mrjbq7/ta-lib
https://python-binance.readthedocs.io/en/latest/

wss://stream.binance.com:9443
https://www.npmjs.com/package/wscat

wscat -c wss://stream.binance.com:9443/ws/btcusdt@trade
wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m

{"e":"trade","E":1648803465066,"s":"BTCUSDT","t":1312007330,"p":"45126.70000000","q":"0.03618000","b":10037666182,"a":10037666102,"T":1648803465065,"m":false,"M":true}

https://www.unixtimestamp.com/

{
    "e":"kline","E":1648804048510,"s":"BTCUSDT",
    "k":{
            "t":1648803900000,
            "T":1648804199999,
            "s":"BTCUSDT",
            "i":"5m",
            "f":1312012621,
            "L":1312014790,
            "o":"45103.11000000",
            "c":"45077.75000000",
            "h":"45113.42000000",
            "l":"45077.75000000",
            "v":"72.92933000",
            "n":2170,
            "x":false,
            "q":"3288447.05229820",
            "V":"35.71042000",
            "Q":"1610217.93818330",
            "B":"0"
        }
}

wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m | tee dataset.text


API KEY sckvM4fgXGXxBpbkeyY9yaXJI1gER0M40nCdI6nPWscN87x2McqfcJIYPVLNEoc5
SECRET KEY RzYvqzjJK82aseutkyYnw0TDbVCxlPGXK7CaLPalncoLpLpGQfakaicGpnT0PgIH

https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference

### Flask
export FLASK_APP=app.py
export FLASK_ENV=development

### Notes
sudo ntpdate ntp.ubuntu.com
sudo ntpdate ntp.ubuntu.com &>/dev/null