def timeline():
    from store_prices import store_prices
    import matplotlib.pyplot as plt
    from datetime import datetime

    # {{date: [lowest price in this day, highest price in this day]}, ...}
    DATA = store_prices()
    # list of all recorded dates
    dates = list(DATA.keys())

    lowest_price = float('inf')
    highest_price = float('-inf')

    # update the highest and the lowest price ever recorded to be able to accommodate chart's y_axis 
    for dictionary in DATA:

        low = DATA[dictionary][0]
        high = DATA[dictionary][1]

        if low < lowest_price:
            lowest_price = low

        if high > highest_price:
            highest_price = high


    x_axis = [date.replace('-', '/') for date in dates]
    y_axis = range(int(lowest_price), int(highest_price) + 1)

    # plot timeline
    return None
