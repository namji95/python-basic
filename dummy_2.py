# "C:\workSpace\pythonBasic\csv"
from faker import Faker
from faker.providers import address, company, date_time, phone_number, person
import pandas as pd

fake = Faker('ko_KR')

class DummyData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.person = []
        self.addr = []
        self.phone = []
        self.company = []
        self.date_time = []

    def add_person(self):
        for i in range(10):
            self.person.append(fake.add_provider(person))

        return self.person

    def create_csv(self):
        person_df = pd.DataFrame(self.person)
        person_df.to_csv(f"{self.file_path}/people.csv", index=False, encoding='utf-8')

        print("CSV 파일이 생성되었습니다.")

if __name__ == '__main__':
    dummy_data = DummyData("C:/workSpace/pythonBasic/csv")
    dummy_data.add_person()
