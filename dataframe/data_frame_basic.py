import pandas as pd


class DataFrameBasic:
    def data_frame_basic(self):
        print("판다스 데이터 프레임 활용 예제")

        print("\n데이터 프레임 생성")
        data = {
            '이름': ['홍길동', '김철수', '이영희'],
            '나이': [25, 30, 22],
            '성별': ['남', '남', '여']
        }
        # 데이터 프레임 생성 방법
        df = pd.DataFrame(data)
        print(df)

if __name__ == '__main__':
    dfb = DataFrameBasic()
    dfb.data_frame_basic()