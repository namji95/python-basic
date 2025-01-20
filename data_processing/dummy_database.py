from sqlalchemy import create_engine

from constants import DBConstants


class DummyDatabase:
    def dummy_database(self):
        db_constants = DBConstants()
        username = db_constants.DB_USERNAME
        password = db_constants.DB_PASSWORD
        host = db_constants.DB_HOST
        port = db_constants.DB_PORT
        database = db_constants.DB_NAME

        engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8mb4")

        return engine