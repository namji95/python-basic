from faker import Faker
import pandas as pd

fake = Faker('ko_KR')

class DummyData:
    def __init__(self, file_path):
        self.person = []
        self.addr = []
        self.date_dummy = []
        self.text_dummy = []
        self.etc_dummy = []
        self.file_path = file_path

    ''' 사람 '''
    def people(self):
        for i in range(100000):
            name = fake.name()  # 이름
            first = name[0]  # 이름 (first)
            last = name[1:]  # 이름 (last)
            email = fake.email()  # 이메일 주소
            phone = fake.phone_number()  # 전화번호

            person_info = {
                'name': name,
                'first': first,
                'last': last,
                'email': email,
                'phone': phone,
            }

            self.person.append(person_info)

        return self.person

    ''' 주소 '''
    def address(self):
        for i in range(99999):
            address = fake.address() # 주소
            split_address = address.split()
            city = split_address[0]  # 도시
            district = split_address[1] # 주
            rest = split_address[2]

            address_data = {
                '주소': address,
                '시': city,
                '군 / 구': district,
                '도로명' : rest,
            }

            self.addr.append(address_data)

        return self.addr

    ''' 날짜 '''
    def date(self):
        for i in range(99999):
            birth = fake.date_of_birth()  # 생년월일
            century = fake.date_this_century()  # 100년 내의 날짜
            month = fake.date_this_month()  # 이번 달 날짜
            year = fake.date_this_year()  # 올해의 날짜
            time = fake.time()  # 랜덤 시간

            date_data = {
                'birth': birth,
                'century': century,
                'month': month,
                'year': year,
                'time': time,
            }

            self.date_dummy.append(date_data)

        return self.date_dummy

    ''' 텍스트 '''
    def text(self):
        for i in range(99999):
            text = fake.text()  # 임의의 텍스트
            sentence = fake.sentence()  # 임의의 문장
            paragraph = fake.paragraph()  # 임의의 단락
            words = fake.words()  # 임의의 단어 목록

            text_data = {
                'text': text,
                'sentence': sentence,
                'paragraph': paragraph,
                'words': words,
            }

            self.text_dummy.append(text_data)

        return self.text_dummy

    ''' 기타 '''
    def etc(self):
        for i in range(99999):
            color = fake.color_name()  # 랜덤 색상 이름
            company = fake.company()  # 회사 이름
            job = fake.job()  # 직업 이름
            password = fake.password()  # 랜덤 암호
            uuid = fake.uuid4()  # 랜덤 UUID4

            etc_data = {
                'color': color,
                'company': company,
                'job': job,
                'password': password,
                'uuid': uuid,
            }

            self.etc_dummy.append(etc_data)

        return self.etc_dummy

    def create_csv(self):
        person_df = pd.DataFrame(self.person)
        person_df.to_csv(f"{self.file_path}/people.csv", index=False, encoding='utf-8')
        address_df = pd.DataFrame(self.addr)
        address_df.to_csv(f"{self.file_path}/address.csv", index=False, encoding='utf-8')
        date_df = pd.DataFrame(self.date_dummy)
        date_df.to_csv(f"{self.file_path}/date.csv", index=False, encoding='utf-8')
        text_df = pd.DataFrame(self.text_dummy)
        text_df.to_csv(f"{self.file_path}/text.csv", index=False, encoding='utf-8')
        etc_df = pd.DataFrame(self.etc_dummy)
        etc_df.to_csv(f"{self.file_path}/etc.csv", index=False, encoding='utf-8')

        print("CSV 파일로 저장되었습니다.")

if __name__ == '__main__':
    dummy_data = DummyData("C:/workSpace/pythonBasic/csv")
    dummy_data.people()
    dummy_data.address()
    dummy_data.date()
    dummy_data.text()
    dummy_data.etc()
    dummy_data.create_csv()