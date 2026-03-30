import os
import requests
api_key=os.getenv("API_KEY")
BASE_URL="https://api.cricapi.com/v1/"

def crickservice_fun(type_data='countries',offset=0):
    URL=BASE_URL+type_data
    response=requests.get(URL,params={
        "apikey":api_key,
        "offset":offset
    },)
    response.raise_for_status()
    return response.json()

def crickservice_info(type_data='series_info',id=0):
    URL=BASE_URL+type_data
    response=requests.get(URL,params={
        "apikey":api_key,
        "id":id
    },)
    print(URL)
    response.raise_for_status()
    return response.json()