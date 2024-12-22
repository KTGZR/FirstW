from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
conn = 'postgresql+psycopg2://postgres:root@db:5432/postgres'

def check_db_connection(database_url):
    try:
        engine = create_engine(database_url)
        with engine.connect() as connection:
            return True
    except SQLAlchemyError as e:
        print(f"Ошибка подключения к БД: {e}")
        return False

if __name__ == "__main__":
    database_url = 'postgresql+psycopg2://postgres:root@db:5432/postgres' 
    if check_db_connection(database_url):
        print("Соединение с БД установлено успешно!")
    else:
        print("Не удалось установить соединение с БД.")