import pandas as pd
import json
from datetime import datetime,timedelta
import requests
from sqlalchemy import create_engine
import sys

#start_date='2022-10-26'
#end_date='2023-10-28'
start_date = sys.argv[1]
end_date = sys.argv[2]
url = "https://api.nasa.gov/neo/rest/v1" 
date_format='%Y-%m-%d'
start_date = datetime.strptime(start_date, date_format)
end_date = datetime.strptime(end_date, date_format)
connection = create_engine("postgresql+psycopg2://postgres:root@localhost:5432/postgres")
current_start = start_date
full_dataframe = pd.DataFrame()

def getDate(url,Date_start,Date_end):
    newurl = url + f'/feed?start_date={Date_start}&end_date={Date_end}&api_key=gaOGNhbzldLgMVfirHiPDhvaoJf9bQFpAxbIdd6b'
    response = requests.get(newurl)
    data = response.json()
    return data

while current_start <= end_date:
    current_end = min(current_start + timedelta(days=6), end_date)
    api_start_date = current_start.strftime(date_format)
    api_end_date = current_end.strftime(date_format)
    data = getDate(url,api_start_date,api_end_date)
    df = pd.DataFrame(data)
    unpackName = df.iloc[:,2]
    unpackName = unpackName.to_list()
    df = pd.DataFrame(unpackName[3])
    newdop = pd.DataFrame(df.iloc[:,0].to_list())
    df.iloc[:,0]=newdop.iloc[:,0]
    newdop = pd.DataFrame(df.iloc[:,6].to_list())
    newdop = pd.DataFrame(newdop.iloc[:,1].to_list())
    df.iloc[:,6] = newdop.iloc[:,1]
    newdop = pd.DataFrame(df.iloc[:,8].to_list())
    newdop = pd.DataFrame(newdop.iloc[:,0].to_list())
    df.iloc[:,8]=newdop.iloc[:,-1]
    del df['links']
    del df['nasa_jpl_url']
    del df['is_sentry_object']
    del df['is_potentially_hazardous_asteroid']
    del df['neo_reference_id']
    del df['sentry_data']
    full_dataframe = pd.concat([full_dataframe,df],ignore_index=True)
    current_start = current_end + timedelta(days=1)
full_dataframe.to_excel("BigData.xlsx")
full_dataframe.to_sql(name='holidays',con=connection,schema="public",if_exists='replace',index = False,method='multi')


