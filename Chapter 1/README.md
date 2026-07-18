# Chapter 1: Products and Markets

This project contains Python implementations of financial concepts introduced in **Chapter 1** from *Paul Wilmott Introduces Quantitative Finance*.

## Compound Interest

### Discrete Compounding

Discrete compounding assumes that interest is paid at fixed intervals (typically once per year). The future value of an investment is calculated using:

$$
A = S(1 + r)^t
$$

where:

- **A** – Future value of the investment
- **S** – Initial principal (spot value)
- **r** – Annual interest rate (expressed as a decimal)
- **t** – Time in years

### Continuous Compounding

When interest is compounded multiple times per year, the future value is given by:

$$
A = S\left(1 + \frac{r}{m}\right)^{mt}
$$

where:

- **A** – Future value of the investment
- **S** – Initial principal (spot value)
- **r** – Annual interest rate (expressed as a decimal)
- **m** – Number of compounding periods per year
- **t** – Time in years

As the number of compounding periods increases, the investment grows more quickly because interest is earned on previously accumulated interest more frequently.

## Forward Price


# Forward Contracts

A forward contract is an agreement between two parties to buy or sell an asset at a predetermined price on a specified future date. Under the assumption of no arbitrage, the fair forward price depends on the current spot price, the risk-free interest rate, the dividend yield, and the time until maturity.

## Fair Forward Price

The theoretical forward price is given by:

$$
F = Se^{(r-q)T}
$$

where:

- **F** – Fair forward price
- **S** – Current spot price of the asset
- **r** – Continuously compounded risk-free interest rate
- **q** – Continuous dividend yield of the asset
- **T** – Time to maturity (in years)

## Python Implementation

This repository implements the forward pricing formula as a Python function:

- `calculate_forward(S, r, q, T)` – Computes the theoretical no-arbitrage forward price using continuous compounding.

The function takes the spot price, risk-free interest rate, dividend yield, and time to maturity, then returns the fair forward price rounded to two decimal places.

### Example

```python
calculate_forward(100, 0.03, 0.01, 5)
```

**Output**

```text
110.52
```

This example calculates the fair price of a five-year forward contract on an asset with a spot price of \$100, a 3% continuously compounded risk-free rate, and a 1% continuous dividend yield.
