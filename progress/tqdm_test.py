from tqdm import tqdm
import time


class TqdmTest:
    def tqdm_test(self):
        print("tqdm 라이브러리를 활용한 예시 코드")

        print("-----tqdm 기초 사용법-----")
        for i in tqdm(range(10), desc="Progressing"):
            time.sleep(0.5)


if __name__ == '__main__':
    tqdmTest = TqdmTest()
    tqdmTest.tqdm_test()