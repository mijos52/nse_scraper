from operator import le
import requests
from pprint import pprint

# Fetches pre-market data from nse-india Website

print("start")

# headers = {
#     'Accept' :'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Cache-Control'  :'max-age=0',
#     'Connection':'keep-alive',
#     'DNT' :'1',
#     'Host':	'www.nseindia.com',
#     'Sec-Fetch-Dest':	'document',
#     'Sec-Fetch-Mode':	'navigate',
#     'Sec-Fetch-Site':	'none',
#     'Sec-Fetch-User':	'?1',
#     'Upgrade-Insecure-Requests':'1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
#                          'like Gecko) '
#                          'Chrome/80.0.3987.149 Safari/537.36'
#         }
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
# length = len(data)
# print(length)
# zero = data[0]
# metadata_zero = zero['metadata']
# symbol_details_zero = {}
# print(type(symbol_details_zero))
# symbol_details_zero = metadata_zero['symbol'] , metadata_zero['lastPrice'], metadata_zero['change'], metadata_zero['pChange']
# print(symbol_details_zero)

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

pprint(sheets_upload)

    

