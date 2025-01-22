from faker import Faker
import random
import pandas as pd
from data_processing.dummy_database import DummyDatabase
from sqlalchemy import MetaData, insert


class DummyDataToDB:
    def dummy_data_to_db(self):
        fake = Faker('ko_KR')
        Faker.seed(1)

        repeat_count = 100000

        names = [fake.name() for _ in range(repeat_count)]
        phones = [
            ('010' +
             '-' +
             str(random.randint(1, 9999)).zfill(4) +
             '-' +
             str(random.randint(1, 9999)).zfill(4))
            for _ in range(repeat_count)
        ]
        emails = [fake.unique.free_email() for _ in range(repeat_count)]
        user_status = [random.choice(['active', 'inactive', 'dormancy']) for _ in range(repeat_count)]
        user_class = [random.choice(['일반', 'Family', 'VIP', 'VVIP']) for _ in range(repeat_count)]
        marketing_agree = [random.choice(['0', '1']) for _ in range(repeat_count)]
        social_login = [random.choice(['google', 'facebook', 'kakao', 'naver']) for _ in range(repeat_count)]
        create_dt = [fake.date_between(start_date='-1y', end_date='today') for _ in range(repeat_count)]

        df = pd.DataFrame({
            'name': names,
            'phone': phones,
            'email': emails,
            'user_status': user_status,
            'user_class': user_class,
            'marketing_agree': marketing_agree,
            'social_login': social_login,
            'create_dt': create_dt
        })

        records = df.to_dict(orient='records')

        dummy_db = DummyDatabase()

        engine = dummy_db.dummy_database()
        with engine.begin() as connection:
            metadata = MetaData()
            metadata.reflect(bind=engine)
            table = metadata.tables.get('users')

            if table is None:
                raise ValueError("Table 'users' does not exist in the database.")

            query = insert(table)
            result_proxy = connection.execute(query, records)
            print(f"{result_proxy.rowcount} rows inserted.")
