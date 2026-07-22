import numpy as np
import matplotlib.pyplot as plt

from long_call import LongCallOption
from long_put import LongPutOption
from short_call import ShortCallOption
from short_put import ShortPutOption
from portfolio import OptionPortfolio


def create_portfolio():

    portfolio = OptionPortfolio()

    options = {
        "Long Call":[], 
        "Short Call": [], 
        "Long Put": [], 
        "Short Put": []
    }

    flag = True

    while flag:
        option_type = input(
            "Enter option type (Long Call, Short Call, Long Put, Short Put): "
        )

        strike = float(input("Enter strike price: "))
        premium = float(input("Enter premium per share: "))
        num_stocks = int(input("Enter number of shares: "))

        print(f"\nOption Type: {option_type}")
        print(f"Strike Price: ${strike:.2f}")
        print(f"Premium: ${premium:.2f}")
        print(f"Number of Shares: {num_stocks}\n")

        if option_type == "Long Call": 
            option_class = LongCallOption 
        elif option_type == "Short Call": 
            option_class = ShortCallOption 
        elif option_type == "Long Put": 
            option_class = LongPutOption 
        else: 
            option_class = ShortPutOption

        new_option = option_class(strike, premium, num_stocks)

        portfolio.add_option(new_option)

        options[option_type].append(new_option)


        again = input(
            "Add another option (yes, no): "
        )

        print(f"\n")

        if again == "no":
            flag = False

    return portfolio, options

def create_graph(portfolio, options):

    stock_prices = np.linspace(50, 150, 500)

    portfolio_profit = portfolio.profit(stock_prices)

    plt.plot(
        stock_prices,
        portfolio_profit,
        label="Portfolio"
    )

    for option_type, option_list in options.items():

        i = 0

        if len(option_list) > 1:
            i = 1

        for option in option_list:

            option_profit = option.profit(stock_prices)

            if i == 0:

                plt.plot(
                    stock_prices,
                    option_profit,
                    label= option_type
                )

            else:

                plt.plot(
                    stock_prices,
                    option_profit,
                    label= option_type + str(i)
                )

                i += 1
    plt.axhline(
        0,
        linestyle="--"
    )

    plt.xlabel(
        "Stock Price at Expiration"
    )

    plt.ylabel(
        "Profit / Loss ($)"
    )

    plt.title(
        "Option Strategy"
    )

    plt.legend()
    plt.grid(True)

    plt.show()



def main():
    portfolio, options = create_portfolio()
    create_graph(portfolio, options)

if __name__ == "__main__":
    main()