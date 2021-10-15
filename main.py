import requests
import sheets_auth

# variables for the url
page_size = 50
min_price = 200
max_price = 50000

response = requests.get(
    f'https://etmarketsapis.indiatimes.com/ET_Stats/gainers?pagesize={page_size}&exchange=nse&pageno=1&sort=intraday'
    f'&sortby=percentchange&sortorder=desc&duration=1d&minprice={min_price}&maxprice='
    f'{max_price}&pricerange=pricerange3')

x = response.json()
y = x["searchresult"]
print(y[0])
ticker_details = []

# TODO : three while loops are used for sorting data (reduce the number of loops)

i = 0
while i < page_size:
    ticker_details.append(y[i])
    i += 1

# Second loop Isolate values needed (changepct , price , volume , week high , sector )
i = 0
ticker_name = []
ticker_volume = []
ticker_Current = []
ticker_Pct = []
ticker_Sector = []
while i < page_size:
    x = dict(ticker_details[i])
    y = "NSE:"+x["ticker"]
    a = x["percentChange"]
    b = x["volume"]
    c = x["current"]
    d = x["sectorName"]
    ticker_name.append(y)
    ticker_volume.append(b)
    ticker_Pct.append(a)
    ticker_Current.append(c)
    ticker_Sector.append(d)
    i += 1

# Make values in the format(nested list) that can be passed to sheets api as (values)
i = 0
values = []

while i < page_size:
    ticker_Quote = [ticker_name[i],ticker_Sector[i],  ticker_Current[i] ,ticker_Pct[i] ,None, None,None,None,None,ticker_volume[i]]
    values.append(ticker_Quote)
    i += 1

sheets_auth.single_Range_Write(values)
