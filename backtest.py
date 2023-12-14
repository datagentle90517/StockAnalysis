def backtest(mode,data,money,fee,manualShort,manualLong,optShortRange1,optShortRange2,optLongRange1,optLongRange2):
    from backtesting import Backtest, Strategy
    from backtesting.lib import crossover
    from backtesting.test import SMA

    class SmaCross(Strategy):
        shortLine = manualShort
        LongLine = manualLong

        def init(self):
            close = self.data.Close
            self.sma1 = self.I(SMA, close, self.shortLine)
            self.sma2 = self.I(SMA, close, self.LongLine)

        def next(self):
            if crossover(self.sma1, self.sma2):
                self.buy()
            elif crossover(self.sma2, self.sma1):
                self.sell()


    bt = Backtest(data, SmaCross,
                  cash=money, commission=fee,
                  exclusive_orders=True)

    if(mode==True):
        output = bt.run()
        print(output)
        bt.plot()
        return output
    elif(mode==False):
        opt_result = bt.optimize(shortLine=range(optShortRange1,optShortRange2, 5),  #將回測機器加入optimize屬性，定義短均線的周期為5~50(每次加5)，長均線的周期為10~120(每次加5)
                            LongLine=range(optLongRange1, optLongRange2, 5),
                            maximize='Equity Final [$]',  #最佳化目標為最終資產最大化
                            constraint=lambda p: p.shortLine < p.LongLine)  #限制n1及n2的範圍，只會計算n1小於n2的情況
        print("最佳化策略")
        print(opt_result)
        return opt_result
