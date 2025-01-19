from tqdm import tqdm
import time


class TqdmTest:
    def tqdm_test(self):
        print("tqdm 라이브러리를 활용한 예시 코드")

        print("\n-----tqdm 기초 사용법-----")
        for i in tqdm(range(5), desc="Progressing"):
            time.sleep(0.1)

        print("\n-----tqdm 기초 사용법-----")
        data = ["A", "B", "C", "D", "E"]
        for idx, value in tqdm(enumerate(data), total=len(data), desc="Enumerating"):
            time.sleep(0.2)



if __name__ == '__main__':
    tqdmTest = TqdmTest()
    tqdmTest.tqdm_test()