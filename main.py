import requests
import sheets_auth
import time
import config
import logging

def log_config()-> None:
    logging.basicConfig(filename=config.LOG_FILE,level=logging.INFO)

def create_log(message:str) -> None:
    logging.info(message)

def make_api_call() -> list[str]:
    create_log('Making API call ')
    response = requests.get(config.API_URL)
    json_response = response.json()
    return json_response["searchresult"]
    
def prep_data(data:list[str]) -> list[str]:
    values:list[str] = []
    create_log('Preparing data')

    for i in data:
      ticker_quote = [i["companyName"], i["current"], i["percentChange"], i["volume"], i["averageVolume"]]
      values.append(ticker_quote)
    return values

def write_to_google_sheets(values:list[str])-> None:
    create_log('writing data to google sheets')
    sheets_auth.volume_shockers_data(values)
    
def main_loop() -> None:
# TODO: Improve this code
    Flag = 0
    while Flag == 0:
        try:
            while True:
                log_config()
                data = make_api_call()
                sheets_data = prep_data(data=data)
                write_to_google_sheets(values = sheets_data)
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


main_loop()

