from tqdm import tqdm
import time


class TqdmTest:
    def tqdm_test(self):
        print("\ntqdm 라이브러리를 활용한 예시 코드")

        print("\n-----tqdm 기초 사용법-----")
        for i in tqdm(range(5), desc="Progressing"):
            time.sleep(0.1)

        print("\n-----tqdm과 enumerate 활용-----")
        data = ["A", "B", "C", "D", "E"]
        for idx, value in tqdm(enumerate(data), total=len(data), desc="Enumerating"):
            time.sleep(0.2)

        print("\n-----tqdm 과 리스트 컴프리헨션 활용-----")
        result = [time.sleep(0.3) or i**2 for i in tqdm(range(5), desc="Calculating")]

if __name__ == '__main__':
    tqdmTest = TqdmTest()
    tqdmTest.tqdm_test()