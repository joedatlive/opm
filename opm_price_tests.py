# opm price test
def price_test(price, bid, ask, option_type, contract_name, last_trade_date):
    assert price > bid, "TEST FAIL: Price does not match market: price is not greater than the bid: %r" % bid
    assert price < ask, "TEST FAIL: Price does not match market: price is not less than the ask: %r" % ask

    if price != 0:
        price = '${:,.2f}'.format(price)
        print("TEST PASS: The value of the", option_type, "stock option for", contract_name, "on date", last_trade_date, "is:", price)
    else:
        print("TEST WARNING: The price is zero, that doesn't seem right")