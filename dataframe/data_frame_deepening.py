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

if __name__ == '__main__':
    data_frame_deepening = DataFrameDeepening()
    data_frame_deepening.data_frame_deepening()