import asyncio
from multiprocessing import Pool

from tqdm.asyncio import tqdm  # 비동기 방식 tqdm 임포트
import threading
import time

from tqdm import tqdm


class TqdmDeepening:
    print("tqdm 라이브러리를 활용한 예시 코드 심화")

    def tqdm_threading(self):
        print("\n----- tqdm과 threading 활용 -----")
        num_tasks = 10
        threads = []

        with tqdm(total=num_tasks, desc="Threading", position=0) as pbar:
            for _ in range(num_tasks):
                thread = threading.Thread(target=self.worker(pbar))
                threads.append(thread)

            for t in threads:
                t.start()

            for t in threads:
                t.join()

    def worker(self, pbar):
        time.sleep(0.1)  # 각 작업이 0.1초 대기
        pbar.update(1)  # 진행률 1 증가

    async def async_task(self, n):
        """비동기 작업을 수행하는 예제 함수"""
        await asyncio.sleep(0.2)  # 비동기 지연 (예제용)

    async def tqdm_async(self):
        tasks = [self.async_task(i) for i in range(1, 6)]  # 비동기 작업 목록

        # tqdm을 사용하여 비동기 태스크 진행률 표시
        progress_bar = tqdm(total=len(tasks), desc="Processing", leave=True)

        # 비동기 작업을 하나씩 실행하면서 진행률 업데이트
        for i, task in enumerate(tasks):
            # 비동기 작업을 실행하고
            await task
            progress_bar.update(1)  # 작업이 완료되면 진행률 업데이트

    def tqdm_multiprocessing(self):
        with Pool(4) as p:
            result = list(tqdm(p.imap(self.process, range(1, 6)), "MultiProcessing", total=5))
            print(result)

    def process(self, x):
        time.sleep(0.3)
        return x**2

if __name__ == '__main__':
    tqdm_deepening = TqdmDeepening()
    tqdm_deepening.tqdm_threading()
    asyncio.run(tqdm_deepening.tqdm_async())
    tqdm_deepening.tqdm_multiprocessing()
