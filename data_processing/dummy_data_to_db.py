from faker import Faker
import random
import pandas as pd

class DummyDataToDB:
    def dummy_data_to_db(self):
        fake = Faker('ko_KR')
        Faker.seed(1)

        repeat_count = 10000

        names = [fake.name() for i in range(repeat_count)]
        phones = [
            ('010' +
             '-' +
             str(random.randint(1, 9999)).zfill(4) +
             '-' +
             str(random.randint(1, 9999)).zfill(4))
            for i in range(repeat_count)
        ]
        emails = [fake.unique.free_email() for i in range(repeat_count)]
        user_status = ['active' for i in range(repeat_count)]
        user_class = [random.choice(['일반', 'Family', 'VIP', 'VVIP']) for i in range(repeat_count)]
        marketing_agree = [random.choice(['0', '1']) for i in range(repeat_count)]
        social_login = [random.choice(['google', 'facebook', 'kakao', 'naver']) for i in range(repeat_count)]
        create_dt = [fake.date_between(start_date='-1y', end_date='today') for i in range(repeat_count)]

        df = pd.DataFrame()
        df['name'] = names
        df['phone'] = phones
        df['email'] = emails
        df['user_status'] = user_status
        df['user_class'] = user_class
        df['marketing_agree'] = marketing_agree
        df['social_login'] = social_login
        df['create_dt'] = create_dt

        print(df) # 데이터 프레임으로 변환된 데이터 출력

        records = df.to_dict(orient='records')
        print(records) # 데이터 프레임으로 변환된 데이터 딕셔너리 형태로 변환 후 출력