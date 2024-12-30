import os
import pandas as pd
from sqlalchemy import create_engine

engine  = create_engine('postgresql+psycopg2://postgres:root@localhost:5432/postgres')
try:
    with engine.connect() as conn:
        print("Подключение успешно установлено")
except Exception as e:
    print(f"Ошибка подключения: {e}")
df = pd.read_sql_table(table_name='holidays',con=engine,schema='public')

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
file_path = os.path.join(parent_dir,"Equipment\data.xlsx")
df.to_excel(file_path)



