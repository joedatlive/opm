import urllib.request
import json
from opm import option_price_model
from opm_price_tests import price_test
from datetime import datetime, date

class Option(object):
    pass

def get_date(timestamp):
    return(date.fromtimestamp(timestamp))

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
        o.expiration = get_date(option_list[i]["expiration"])
        o.days_to_expiration = (o.expiration - date.today()).days
        o.implied_volatility = option_list[i]["impliedVolatility"]
        o.risk_free_interest_rate = option_list[i]["openInterest"]
        o.bid = option_list[i]["bid"]
        o.ask = option_list[i]["ask"]
        o.contract_symbol = option_list[i]["contractSymbol"]
        o.last_trade_date = get_date(option_list[i]["lastTradeDate"])
        price = option_price_model(o.option_place, o.option_type, o.strike_price, o.stock_price, o.days_to_expiration, o.implied_volatility, o.risk_free_interest_rate)
        print("expiration:", o.expiration)
        print("days to exp:", o.days_to_expiration)
        print("last trade date:", o.last_trade_date)
        price_test(price, o.bid, o.ask, o.option_type, o.contract_symbol, o.last_trade_date)
      
        i += 1

get_option_data("calls")
