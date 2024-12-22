import sys
import requests
import pandas as pd
from sqlalchemy import create_engine
usr = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2023-10-26&end_date=2023-10-28&api_key=gaOGNhbzldLgMVfirHiPDhvaoJf9bQFpAxbIdd6b"
connection = create_engine("postgresql+psycopg2://postgres:root@localhost:5432/postgres")
response = requests.get(usr)
data = response.json()
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
print(df)
# for col in df:  
#     try:
#       df[col] = df[col].str.encode('utf-8').str.decode('utf-8')
#     except:

#       print(f"Не удалось кодировать столбец {col}")
#       continue 
# for col in df:
#   df[col] = df[col].str.replace(r'[^\x00-\x7F]+', '', regex=True)
# df.to_csv("end.csv")
df.to_sql(name='holidays',con=connection,schema="public",if_exists='replace',index = False,method='multi')
