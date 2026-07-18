import numpy as np
import matplotlib.pyplot as plt

def discretely_compounded(S, r, t):
    '''
    Takes as input:
        S <- starting principle
        r <- annual interest rate
        t <- number of years
    Returns: Principle after t years
    '''
    interest = (1+r)**t
    return S * interest

def continuously_compounded(S, r, m, t):
    '''
    Takes as input:
        S <- starting principle
        r <- annual interest rate
        m <- number of compounding periods per year
        t <- number of years
    Returns: Principle after t years
    '''
    interest = (1 + r/m)**(m*t)
    return S * interest

def main():

    # Parameters
    S = 1000
    r = 0.05
    m = 12
    years = 20

    t = np.linspace(0, years, 100)

    discrete = discretely_compounded(S, r, t)
    compound = continuously_compounded(S, r, m, t)

    plt.plot(t, discrete, label="Discrete (Annual)")
    plt.plot(t, compound, label="Compound (Monthly)")
    plt.xlabel("Time (years)")
    plt.ylabel("Investment Value ($)")
    plt.title("Interest Growth by Type")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()