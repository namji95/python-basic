from tqdm import tqdm
import threading
import time

class TqdmDeepening:
    def tqdm_deepening(self):
        print("tqdm 라이브러리를 활용한 예시 코드 심화")

        print("\n-----tqdm과 threading 활용-----")
        threads = []
        num_tasks = 10
        with tqdm(total=num_tasks, desc="Threading", position=0) as pbar:
            for _ in range(num_tasks):
                thread = threading.Thread(target=self.worker(pbar))
                threads.append(thread)

            for t in threads:
                t.start()

            for t in threads:
                t.join()

    def worker(self, pbar):
        time.sleep(0.1)  # 각 작업이 2초 대기
        pbar.update(1)  # 작업 완료 시 진행률 1 업데이트

if __name__ == '__main__':
    tqdmDeepening = TqdmDeepening()
    tqdmDeepening.tqdm_deepening()
