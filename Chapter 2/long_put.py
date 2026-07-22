import numpy as np
import matplotlib.pyplot as plt

class LongPutOption:

    def __init__(self, strike, premium, num_stocks):
        self.strike = strike
        self.premium = premium
        self.num_stocks = num_stocks

    def payoff(self, stock_price):
        return np.maximum(self.strike - stock_price, 0) * self.num_stocks
    
    def profit(self, stock_price):
        return self.payoff(stock_price) - self.premium * self.num_stocks
