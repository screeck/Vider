def prices_spectrum():
    from bs4 import BeautifulSoup
    import requests
    import json
    from datetime import date
    import time

    today = str(date.today())
    # url of vider site
    url = "https://www.ceneo.pl/81184639"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    # find html tags named script
    links = soup.find("script")
    # extract offers' info
    offers = json.loads(links.text)['offers']
    # segregates price variations by date, from lowest to highest price
    current_spectrum = {} # {'2020-01-04': [2012.0, 2888.0]}

    lowest_price = float('inf')

    highest_price = float('-inf')

    if offers['availability'] == 'InStock':

        if offers['lowPrice'] < lowest_price:
            lowest_price = offers['lowPrice']

        if offers['highPrice'] > highest_price:
            highest_price = offers['highPrice']

    current_spectrum[today] = [lowest_price, highest_price]

    return current_spectrum
