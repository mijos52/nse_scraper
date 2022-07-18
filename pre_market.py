import requests
from sheets_auth import pre_market_data



print("start")

baseurl = "https://www.nseindia.com/"
url = f"https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) '
                         'Chrome/80.0.3987.149 Safari/537.36',
           'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
session = requests.Session()
request = session.get(baseurl, headers=headers, timeout=5)
cookies = dict(request.cookies)
response = requests.get('https://www.nseindia.com/api/market-data-pre-open?key=NIFTY' , headers=headers ,cookies=cookies)
result = response.json()

data = result["data"]

symbol = []
lastPrice = []
change = []
pChange = []
meta_data = []
ticker_details = []
sheets_data = []
sheets_upload = []


for i in data :
    meta_data.append(i['metadata'])
    ticker_details.append(i['detail'])
  

for i in meta_data :
    
    symbol.append(i['symbol'])
    lastPrice.append(i['lastPrice'])
    change.append(i['change'])
    pChange.append(i['pChange'])

for i in meta_data :
    sheets_data = [i['symbol'] , i['lastPrice'] , i['change'] ,i['pChange']  ]
    sheets_upload.append(sheets_data)

pre_market_data(sheets_upload)
