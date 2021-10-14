import requests

page_size = 25

response = requests.get(
    f'https://etmarketsapis.indiatimes.com/ET_Stats/gainers?pagesize={page_size}&exchange=nse&pageno=1&sort=intraday&sortby=percentchange&sortorder=desc&duration=1d')

x = response.json()
y = x["searchresult"]
print(len(y))
ticker_details = []
ticker_name = []
# for i in y:
i = 0
while i < page_size:
    ticker_details.append(y[i])
    i += 1

# Second loop Isolate values needed (changepct , price , volume , week high , )
i = 0
while i < page_size:
    x = dict(ticker_details[i])
    y = x["ticker"]
    print(i, ":", y)
    i += 1
