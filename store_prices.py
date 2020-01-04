def store_prices():
    '''Returns history of stock like this: {{date: [lowest price in this day, highest price in this day]}, ...}'''
    from prices_spectrum import prices_spectrum
    
    # prices variation
    DATA = {}
    DATA.update(prices_spectrum())

    return DATA
