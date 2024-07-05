import pandas as pd


class DataFrameDeepening:
    def data_frame_deepening(self):
        print("판다스 데이터 프레임 활용 예제 심화")

        print("\n--------------데이터 프레임 그룹화 및 집계--------------")
        # 예시 데이터 생성
        data = {
            '부서': ['IT', 'HR', 'IT', 'HR', 'IT', 'HR'],
            '직원': ['홍길동', '김철수', '이영희', '박민수', '최지은', '장소연'],
            '나이': [25, 30, 22, 35, 28, 24],
            '급여': [5000, 4000, 4500, 4200, 5500, 3800]
        }
        df = pd.DataFrame(data)

        # 부서별로 급여의 평균을 구합니다.
        grouped = df.groupby('부서')['급여'].mean()
        print(f"부서별 급여 평균:\n{grouped}")

        print("\n--------------데이터 프레임 결측치 처리--------------")
        # 결측치를 포함한 데이터 생성
        data_with_na = {
            '이름': ['홍길동', '김철수', '이영희', None, '최지은'],
            '나이': [25, 30, None, 35, 28],
            '성별': ['남', '남', '여', '남', '여'],
            '급여': [5000, 4000, 4500, 4200, None]
        }
        df_with_na = pd.DataFrame(data_with_na)

        #결측치가 있는 행 제거
        df_no_na = df_with_na.dropna()
        print(f"결측치가 제거된 데이터:\n{df_no_na}")

        # 결측치를 각 열의 평균값으로 채우기
        df_filled = df_with_na.fillna(df_with_na.mean(numeric_only=True))
        print(f"\n결측치를 평균으로 채운 데이터:\n{df_filled}")

if __name__ == '__main__':
    data_frame_deepening = DataFrameDeepening()
    data_frame_deepening.data_frame_deepening()