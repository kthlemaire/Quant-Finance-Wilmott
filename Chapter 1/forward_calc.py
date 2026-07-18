import numpy as np

def calculate_forward(S, r, q, T):
    '''
    Takes as input:
        S <- spot price
        r <- interest rate
        q <- dividend yield
        T <- maturity
    Returns: Fair forward price
    '''

    F = S * np.exp((r-q)*(T))
    return round(F, 2)

def main():
    print(calculate_forward(100, 0.03, 0.01, 5))

if __name__ == '__main__':
    main()