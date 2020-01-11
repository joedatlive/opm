import urllib.request
import json
from opm import option_price_model
from opm_price_tests import price_test

class Option(object):
    pass

def get_option_data(puts_or_calls):
    # pull down json with option data from yahoo finance
    r = urllib.request.urlopen("https://query2.finance.yahoo.com/v7/finance/options/msft").read()
    d = json.loads(r)
    # create an option list object from the options in the json
    option_list = d["optionChain"]["result"][0]["options"][0][puts_or_calls]
    #instantiate an obiect to store the attributes for each option
    o = Option()
    i = 0
    while i < len(option_list):
        o.option_place = "american" # only looking up us stocks on yahoo for this test
        if puts_or_calls == "calls": # check for calls being passed in and if so, set to calls
            o.option_type = "call"
        if puts_or_calls == "puts": # check for calls being passed in and if so, set to calls
            o.option_type = "put"
        o.strike_price = option_list[i]["strike"]
        o.stock_price = option_list[i]["lastPrice"]
        o.days_to_expiration = option_list[i]["expiration"]
        o.implied_volatility = option_list[i]["impliedVolatility"]
        o.risk_free_interest_rate = option_list[i]["openInterest"]
        o.bid = option_list[i]["bid"]
        o.ask = option_list[i]["ask"]
        o.contract_symbol = option_list[i]["contractSymbol"]
        o.last_trade_date = option_list[i]["lastTradeDate"]
        price = option_price_model(o.option_place, o.option_type, o.strike_price, o.stock_price, o.days_to_expiration, o.implied_volatility, o.risk_free_interest_rate)
        print("days to exp:", o.days_to_expiration)
        print("last trade date:", o.last_trade_date)
        price_test(price, o.bid, o.ask, o.option_type, o.contract_symbol, o.last_trade_date)
      
        i += 1

get_option_data("calls")



"""
Here is a sample option:
"contractSymbol": "MSFT200103C00125000",
"strike": 125.0,
"currency": "USD",
"lastPrice": 31.92,
"change": -1.3799992,
"percentChange": -4.1441417,
"volume": 1,
"openInterest": 2,
"bid": 31.45,
"ask": 34.1,
"contractSize": "REGULAR",
"expiration": 1578009600,
"lastTradeDate": 1577811600,
"impliedVolatility": 1.171879140625,
"inTheMoney": true
"""
# iterating through options list and printing last prices


# get the option paramenters from the json for each call option

# test the opm function for each call option

# count success and fails

# output successes and fails

# to print out json to see data uncomment next 4 lines
#with open("options.json", "w") as json_data:
#    json.dump(d, json_data)
#    print("Info: writing json to file options.json")
#print("Done")



