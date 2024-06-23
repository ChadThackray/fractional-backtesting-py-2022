import datetime
import pandas_ta as ta

from backtesting import Backtest
from backtesting import Strategy
from backtesting.lib import crossover
from backtesting.test import GOOG

print(GOOG)

factor = 1000000

GOOG.Open /= factor
GOOG.High /= factor
GOOG.Low /= factor
GOOG.Close/= factor
GOOG.Volume *= factor

print(GOOG)

class RsiOscillator(Strategy):

    upper_bound = 70
    lower_bound = 30
    rsi_window = 14

    # Do as much initial computation as possible
    def init(self):
        self.rsi = self.I(ta.rsi, self.data.Close.s, self.rsi_window)

    # Step through bars one by one
    def next(self):

        if crossover(self.rsi, self.upper_bound):
            self.position.close()

        elif crossover(self.lower_bound, self.rsi):
            if not self.position:
                self.buy()

bt = Backtest(GOOG, RsiOscillator, cash=1000, commission=.002)
stats = bt.run()
print(stats)

#bt.plot()

trades = stats._trades

trades.EntryPrice *= factor
trades.ExitPrice *= factor
trades.Size /= factor

print(trades)











