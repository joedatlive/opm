from math import sqrt, exp, log, erf
import numpy

# create a function to return the theoretical value of a stock option
# info on Black-Scholes: http://janroman.dhis.org/stud/I2014/BS2/BS_Daniel.pdf
def option_price_model(american_or_european, put_or_call, strike_price, stock_price, days_to_expiration, implied_volatility, risk_free_interest_rate):
    price = 0
    if american_or_european == "american":
        d1 = (log(float(stock_price)/strike_price) + (risk_free_interest_rate + implied_volatility ** 2 / 2.) * days_to_expiration) / (implied_volatility * sqrt(days_to_expiration))
        d2 = d1 - implied_volatility * sqrt(days_to_expiration)
        if put_or_call == "call":
            price = stock_price * normcdf(d1) - strike_price * exp(-risk_free_interest_rate * days_to_expiration) * normcdf(d2)
        else:
            if put_or_call == "put":
                price = strike_price * exp(-risk_free_interest_rate * days_to_expiration) * normcdf(d2) - stock_price * normcdf(d1) 
            else:
                print("info: put or call not detected.  Assuming put.")
                price = strike_price * exp(-risk_free_interest_rate * days_to_expiration) * normcdf(d2) - stock_price * normcdf(d1) # same as three lines up = prolly a better way.
    else:
        N = 10
        dt = days_to_expiration/N
        u = (exp(implied_volatility * sqrt(dt)))
        d = 1/u
        p = (exp(risk_free_interest_rate*dt)-d)/(u-d)
        
        price_tree = numpy.zeros([N + 1, N + 1])

        for i in range(N+1):
            for j in range(i+1):
                price_tree[j, i] = stock_price*(d**j)*((u**(i-j)))
        option = numpy.zeros([N+1, N+1])
        option[:, N] = numpy.maximum(numpy.zeros(N+1), price_tree[:, N] - strike_price)

        #options price at t=0
        for i in numpy.arange(N-1, -1, -1):
            for j in numpy.arange(0, i+1):
                option[j,i] = exp(-risk_free_interest_rate*dt)*(p*option[j, i+1]+(1-p)*option[j+1, i+1])
        price = option[0,0]
    
    return price
    

def normcdf(x):
    return (1.0 + erf(x / sqrt(2.0))) / 2.0
