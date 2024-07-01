import pandas as pd


class DataFrameBasic:
    def data_frame_basic(self):
        print("판다스 데이터 프레임 활용 예제\n")

        print("--------------데이터 프레임 생성--------------")
        data = {
            '이름': ['홍길동', '김철수', '이영희'],
            '나이': [25, 30, 22],
            '성별': ['남', '남', '여']
        }
        # 데이터 프레임 생성 방법
        df = pd.DataFrame(data)
        print(f"데이터 프레임 생성:\n{df}")

        print("\n--------------데이터 프레임 기본 정보 확인--------------")
        # 데이터 프레임 정보 출력
        print(f"df.info():\n{df.info()}")
        # 데이터 프레임의 통계 요약 출력
        print(f"\ndf.describe():\n{df.describe()}")

        print("\n--------------데이터 선택 및 필터링--------------")
        # 특정 열 선택
        print(f"특정 열 선택:\n{df['이름']}")
        # 여러 열 선택
        print(f"\n여러 열 선택:\n{df[['이름', '나이']]}")
        # 조건에 맞는 행 필터링
        print(f"\n조건에 맞는 행 필터링:\n{df[df['나이'] > 25]}")

        print("\n--------------데이터 추가 및 삭제--------------")
        df['국가'] = ['한국', '한국', '한국']
        print(f"데이터 추가:\n{df}")
        df = df.drop('국가', axis=1)
        print(f"열 삭제:\n{df}")

if __name__ == '__main__':
    dfb = DataFrameBasic()
    dfb.data_frame_basic()