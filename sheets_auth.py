from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime
import config


cred = service_account.Credentials.from_service_account_file(
    config.SERVICE_ACCOUNT_FILE, scopes=config.SCOPES)

service = build('sheets', 'v4', credentials=cred)
sheet = service.spreadsheets()


# Write data into google sheets
def volume_shockers_data(values):

    body = {'values': values}
    result = service.spreadsheets().values().update(spreadsheetId=config.SHEET_ID, range=config.SHEET_RANGE_ONE,
                                                    valueInputOption='USER_ENTERED',
                                                    body=body).execute()
    print('Success! {0} cells updated.'.format(result.get('updatedCells')))
    print(datetime.now(), '\n')

# Pre_market data form nseindia website
def pre_market_data(values):

    body = { 'values': values}
    result = service.spreadsheets().values().update(spreadsheetId=config.SHEET_ID, range=config.SHEET_RANGE_TWO,
                                                    valueInputOption='USER_ENTERED',
                                                    body=body).execute()
    print('Success! {0} cells updated.'.format(result.get('updatedCells')))
    print(datetime.now(), '\n')


