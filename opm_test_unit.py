#static unit test file for opm.py
#data from yaho finance https://finance.yahoo.com/quote/msft/options/

from opm import option_price_model
from opm_price_tests import price_test
from datetime import date

contract_name = "MSFT191220C00070000"	
last_trade_date = "2019-12-13 2:12PM EST"

option_date = date(2019,12,13)
option_place = "european"
option_type = "call"
strike = 70.00
last_price = 84.55
expiration = date(2019,12,20)
bid = 83.45
ask = 85.70
change = 2.00
percent_change = 2.42
volume = 15
open_interest = 14
implied_volatility = 2.375

days_to_expiration =  (expiration - option_date).days

#calculate risk free interest rate
#maybe use libor or for american stocks use -tbill rate for the same term annualized.  For testing we will use 1.92 from here: https://www.macrotrends.net/2515/1-year-libor-rate-historical-chart

risk_free_interest_rate = 1.92

#call function 
price = option_price_model(option_place, option_type, strike, last_price, days_to_expiration, implied_volatility, risk_free_interest_rate)

price_test(price, bid, ask, option_type, contract_name, last_trade_date)