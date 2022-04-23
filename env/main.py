import requests
import sheets_auth
import time
from pprint import pprint

# variables for the url
page_size = 2
min_price = 100
max_price = 3000

print(f'page_size = {page_size},min_price = {min_price},max_price = {max_price} \n ')


def main():
    print('1.fetching data')
    response = requests.get(
        f'https://etmarketsapis.indiatimes.com/ET_Stats/gainers?pagesize={page_size}&exchange=nse&pageno=1'
        f'&sort=intraday&sortby=percentchange&sortorder=desc&duration=1d&minprice={min_price}&maxprice='
        f'{max_price}&pricerange=pricerange3')

    x = response.json()
    pprint(x)
    y = x["searchresult"]
    print('2.url fetch complete')

    # TODO : three while loops are used for sorting data (reduce the number of loops)
    ticker_details = []
    i = 0
    while i < page_size:
        ticker_details.append(y[i])
        i += 1

    # Second loop Isolate values needed (changepct , price , volume , week high , sector )
    i = 0
    ticker_name = []
    ticker_volume = []
    ticker_current = []
    ticker_pct = []
    ticker_sector = []
    while i < page_size:
        x = dict(ticker_details[i])
        y = "NSE:" + x["ticker"]
        a = x["percentChange"]
        b = x["volume"]
        c = x["current"]
        d = x["sectorName"]
        ticker_name.append(y)
        ticker_volume.append(b)
        ticker_pct.append(a)
        ticker_current.append(c)
        ticker_sector.append(d)
        i += 1

    # Make values in the format(nested list) that can be passed to sheets api as (values)
    i = 0
    values = []

    while i < page_size:
        ticker_quote = [ticker_name[i], ticker_sector[i], ticker_current[i], ticker_pct[i], None, None, None, None,
                        None,
                        ticker_volume[i]]
        values.append(ticker_quote)
        i += 1
    print('3.value prepared Handover to sheets api')

    sheets_auth.single_range_write(values)

  


# one minute delay (0 seconds delay code execution delay 23 seconds)
# Handle internet connection error

# TODO: Improve this code
Flag = 0
while Flag == 0:
    try:
        while True:
            main()
            Flag = 1
            time.sleep(30)
    except requests.ConnectionError:
        print("--server connection failed--")
        Flag = 0
        time.sleep(5)

    except ConnectionResetError:
        print("--Network connection was shut down--")
        Flag = 0
        time.sleep(5)
