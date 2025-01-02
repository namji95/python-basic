# for 예제 10개
# iterable
# iterable - list
class ForEx:
    def iterable_list(self):
        print("리스트를 활용한 for문 예제 1")
        fruits = ["apple", "banana", "cherry"]
        for fruit in fruits:
            print(f"과일 리스트를 이용한 for문 : {fruit}")

if __name__ == '__main__':
    for_ex = ForEx()
    for_ex.iterable_list()