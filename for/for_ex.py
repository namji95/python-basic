# for 예제 10개
# iterable
# iterable - list
class ForEx:
    def iterable_list(self):
        print("리스트를 활용한 for문 예제 1")
        fruits = ["apple", "banana", "cherry"]
        for fruit in fruits:
            print(f"과일 리스트를 이용한 for문 : {fruit}")

        print("\n문자열을 활용한 for문 예제 2")
        word = "Python"
        for char in word:
            print(f"문자열을 이용한 for문 : {char}")

        print("\n튜플을 활용한 for문 예제 3")
        coordinates = [(1, 2), (3, 4), (5, 6)]
        for x, y in coordinates:
            print(f"튜플을 이용한 for문 : {x}, ")

if __name__ == '__main__':
    for_ex = ForEx()
    for_ex.iterable_list()