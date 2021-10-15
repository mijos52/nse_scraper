from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'key.json'

sheet_ID = '12TlM7JEPz9UPLjQ_XbN0qdxMOOSwW1f4bB8rYN_BaNg'
range = "Sheet1!A2:Z1000"

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Read data from google sheets
def single_Range_Read(range):
    result = sheet.values().get(spreadsheetId=sheet_ID, range=range).execute()
    rows = result.get('values', [])
    print('{0} rows retrieved.'.format(len(rows)))
    print(rows)


# Write data into google sheets
def single_Range_Write(values):
    value_Input = 'USER_ENTERED'

    body = {
        'values': values
    }
    result = service.spreadsheets().values().update(spreadsheetId=sheet_ID, range=range, valueInputOption=value_Input,
                                                body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))
    print(result)


