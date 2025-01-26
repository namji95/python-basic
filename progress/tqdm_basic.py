import pandas as pd
from tqdm import tqdm
import time


class TqdmBasic:
    def tqdm_basic(self):
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

        print("\n-----tqdm과 map 활용-----")
        numbers = range(5)
        list(tqdm(map(lambda _: self.process(), numbers), total=len(numbers), desc="Map processing"))

        print("\n-----tqdm과 pandas 활용-----")
        tqdm.pandas(desc="DataFrame processing")

        df = pd.DataFrame({"numbers": numbers})
        df['numbers'].progress_apply(lambda x: time.sleep(0.5) or x**2)

    def process(self):
        time.sleep(0.4)

if __name__ == '__main__':
    tqdmTest = TqdmBasic()
    tqdmTest.tqdm_basic()