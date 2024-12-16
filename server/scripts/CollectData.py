import pandas as pd
from sqlalchemy import create_engine

engine  = create_engine("postgresql+psycopg2://postgres:root@db:5432/postgres")

df = pd.read_sql_table("Holidays",engine,schema="public")

writer = pd.ExcelWriter('./Equipment/data.xlsx',engine='openpyxl',mode="a",if_sheet_exists="overlay",date_format='%d.%m.%y',datetime_format='%d.%m.%y')

df.to_excel(writer,sheet_name="Holidays")

pd.read_json('./Equipment/data.json').to_excel('./Equipment/data.xlsx',index=False)


