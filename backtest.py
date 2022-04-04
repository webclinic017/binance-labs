import backtrader as bt

cerebro = bt.Cerebro()
data = bt.feeds.GenericCSVData(dataname='daily-2022.csv', dtformat=2)
cerebro.adddata(data)
cerebro.run()
cerebro.plot()
