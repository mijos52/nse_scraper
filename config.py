PAGE_SIZE = 50
MIN_PRICE = 500
MAX_PRICE = 2000
API_URL = f'https://etmarketsapis.indiatimes.com/ET_Stats/volumeshocker?'
f'pagesize={PAGE_SIZE}&exchange=50&pageno=1&service=volumeshocker&sortby'
f'volumepercentagechange&sortorder=desc&avgvolumeover=DAY_15&pricerange=pricerange2&minprice={MIN_PRICE}&maxprice={MAX_PRICE}&index=2371'
LOG_FILE = './logs/logs.txt'

"""configuration for sheets_auth.py"""

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'key.json'
SHEET_ID = '12TlM7JEPz9UPLjQ_XbN0qdxMOOSwW1f4bB8rYN_BaNg'
SHEET_RANGE_ONE = "Sheet1!A2:Z1000"
SHEET_RANGE_TWO = "Sheet2!A2:Z1000"