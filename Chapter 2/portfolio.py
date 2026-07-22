import numpy as np

class OptionPortfolio:

    def __init__(self):
        self.options = []

    def add_option(self, option):
        self.options.append(option)

    def profit(self, stock_price):
        total_profit = np.zeros_like(
            stock_price,
            dtype=float
        )

        for option in self.options:
            total_profit += option.profit(stock_price)

        return total_profit
    


