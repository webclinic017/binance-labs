import numpy
import talib
from numpy import genfromtxt

# close = numpy.random.random(100)
# print(close)

# moving_average = talib.SMA(close, timeperiod=10)
# print(moving_average)

my_data = genfromtxt('15minutes.csv', delimiter=',')
print(my_data)

close = my_data[:, 4]
print(close)

rsi = talib.RSI(close)
print(rsi)
