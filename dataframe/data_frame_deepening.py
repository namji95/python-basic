import pandas as pd
import matplotlib.pyplot as plt


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

        print("\n--------------데이터 프레임 조건부 변환 및 필터링--------------")
        # 직원들의 급여를 10% 인상
        df['급여'] = df['급여'].apply(lambda x: x * 1.1 if x >= 4200 else x)
        print(f"급여를 10% 인상한 데이터:\n{df}")

        # 나이가 30 이상인 직원만 필터링
        filtered_df = df[df['나이'] >= 30]
        print(f"\n나이가 30 이상인 직원들:\n{filtered_df}")

        print("\n--------------데이터 프레임을 다른 형식으로 변환--------------")
        # 데이터 프레임을 CSV 파일로 저장
        df.to_csv(r'C:\WorkSpace\python-basic\data\employee_data.csv', index=False)
        print("데이터 프레임을 CSV 파일로 변환 후 python-baisc의 data 패키지에 저장했습니다.")

        # 데이터 프레임을 Excel 파일로 저장
        df.to_excel(r'C:\WorkSpace\python-basic\data\employee_data.xlsx', index=False)
        print("데이터 프레임을 Excel 파일로 변환 후 python-baisc의 data 패키지에 저장했습니다.")

        print("\n--------------데이터 프레임으로 피벗 테이블 생성--------------")
        pivot_table = df.pivot_table(values='나이', index='부서', aggfunc='mean')
        # 부서별로 나이의 평균을 구하는 피벗 테이블 생성
        print(f"부서별 나이 평균 피벗 테이블:\n{pivot_table}")

        print("\n--------------데이터 프레임으로 데이터 시각화--------------")
        grouped_df = df.groupby('부서')['급여'].mean()

        # Window 환경 한글 설정
        plt.rc('font', family='Malgun Gothic')
        # 음수가 깨지지 않도록 설정
        plt.rcParams['axes.unicode_minus'] = False
        # 그래프 형태
        grouped_df.plot(kind='bar')
        # 제목
        plt.title('부서별 평균 급여')
        # x축
        plt.xlabel('부서')
        # y축
        plt.ylabel('평균 급여')
        # View
        plt.show()

if __name__ == '__main__':
    data_frame_deepening = DataFrameDeepening()
    data_frame_deepening.data_frame_deepening()