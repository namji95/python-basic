from data_processing.dummy_data import DummyTest
from data_processing.dummy_data_to_db import DummyDataToDB

if __name__ == '__main__':
    dummy_data_to_db = DummyDataToDB()
    dummy_data_to_db.dummy_data_to_db()