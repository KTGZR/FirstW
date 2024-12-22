import sys
import requests
import pandas as pd
from sqlalchemy import create_engine

url =  "https://api.nasa.gov/neo/rest/v1" 
Date_start = sys.argv[1]
Date_end = sys.argv[2]
connection = create_engine("postgresql+psycopg2://postgres:root@db:5432/postgres")

def getDate(url,Date_start,Date_end):
    newurl = url + f'/feed?start_date={Date_start}&end_date={Date_end}&api_key=gaOGNhbzldLgMVfirHiPDhvaoJf9bQFpAxbIdd6b'
    response = requests.get(newurl)
    data = response.json()
    return data

data = getDate(url,Date_start,Date_end)
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
df.to_sql(name='holidays',con=connection,schema="public",if_exists='replace',index = False,method='multi')

