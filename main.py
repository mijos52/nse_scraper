import requests
import sheets_auth
import time



# variables for the url
page_size = 50
min_price = 100
max_price = 5000

print(f'page_size = {page_size},min_price = {min_price},max_price = {max_price} \n ')


def main():
    print('1.fetching data')
    response = requests.get(
        f'https://etmarketsapis.indiatimes.com/ET_Stats/volumeshocker?'
f'pagesize={page_size}&exchange=50&pageno=1&service=volumeshocker&sortby'
f'volumepercentagechange&sortorder=desc&avgvolumeover=DAY_15&pricerange=pricerange2&minprice={min_price}&maxprice={max_price}&index=2371')


    x = response.json()
  
    y = x["searchresult"]
    items_no = len(y)
    print('2.url fetch complete')

    # TODO : three while loops are used for sorting data (reduce the number of loops)
    ticker_details = []
    i = 0
    while i < items_no:
        ticker_details.append(y[i])
        i += 1

    # Second loop Isolate values needed (changepct , price , volume , week high , sector )
    i = 0
    ticker_name = []
    ticker_ltp = []
    ticker_change = []
    ticker_volume = []
    ticker_volumeavg = []
    while i < items_no:
        x = dict(ticker_details[i])
        y = x["companyName"]
        a = x["current"]
        b = x["percentChange"]
        c = x["volume"]
        d = x["averageVolume"]
        ticker_name.append(y)
        ticker_ltp.append(b)
        ticker_change.append(a)
        ticker_volume.append(c)
        ticker_volumeavg.append(d)
        i += 1

    # Make values in the format(nested list) that can be passed to sheets api as (values)
    i = 0
    values = []

    while i < items_no:
        ticker_quote = [ticker_name[i], ticker_change[i], ticker_ltp[i], ticker_volume[i], ticker_volumeavg[i]
                        ]
        values.append(ticker_quote)
        i += 1
    print('3.value prepared Handover to sheets api')

    # sheets_auth.delete_data()
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
