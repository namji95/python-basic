from faker import Faker

class DummyTest:
    def dummy_test(self):
        fake = Faker('ko_KR')  # locale 정보 설정
        Faker.seed()  # 초기 seed 설정
        name_list = []
        email_list = []

        repeat_count = 10
        for i in range(repeat_count):
            name_list.append(fake.name()) # Faker를 이용하여 랜덤 이름 생성 후 리스트에 담기

        for i in range(repeat_count):
            email_list.append(fake.unique.free_email()) # Faker를 이용하여 랜덤 고유 이메일 생성 후 리스트에 담기

        print("랜덤 이름: ", name_list)
        print("랜덤 이메일: ", email_list)

if __name__ == '__main__':
    dummy_test = DummyTest()
    dummy_test.dummy_test()