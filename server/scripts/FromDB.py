import sys
import requests
import pandas as pd
from sqlalchemy import create_engine

url =  "https://openholidaysapi.org" 
Date_start = sys.argv[1]
Date_end = sys.argv[2]
connection = create_engine("postgresql+psycopg2://postgres:root@db:5432/postgres")

def getDate(url,Date_start,Date_end):
    newurl = url + f'/PublicHolidays?countryIsoCode=BE&languageIsoCode=EN&validFrom={Date_start}&validTo={Date_end}'
    response = requests.get(newurl)
    data = response.json()
    return data

data = getDate(url,Date_start,Date_end)
df = pd.DataFrame(data)
unpackName = df.iloc[:,4]
unpackName = unpackName.to_list()
newdf = pd.DataFrame(unpackName[0])
for i in range(1,unpackName.__len__()):
    temp = pd.DataFrame(unpackName[i])
    newdf.loc[i] = temp.iloc[0]
df.iloc[:,4] = newdf.iloc[:,1]
print(df)


df.to_sql("Holidays",connection,schema="public",if_exists='replace')

