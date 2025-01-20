from faker import Faker

class DummyTest:
    def dummy_test(self):
        fake = Faker('ko_KR')  # locale 정보 설정
        Faker.seed()  # 초기 seed 설정

        name = fake.name()  # 해당 변수 호출 시 랜덤으로 생성된 이름 출력
        print(name)

        email = fake.email()  # 해당 변수 호출 시 랜덤으로 생성된 이메일 출력
        print(email)

        repeat_count = 10000  # 더미 데이터 생성 개수 설정
        emails = [fake.unique.free_email() for i in range(repeat_count)]  # repeat_count 만큼 유니크한 이메일 리스트로 생성
        print(len(emails))
        print(emails)