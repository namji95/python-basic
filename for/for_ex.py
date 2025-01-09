# 리스트를 활용한 for문 예제
print("리스트를 활용한 for문 예제 1")
# 리스트: 여러 값을 하나의 변수에 담을 수 있는 자료구조
# fruits 리스트에는 과일 이름들이 저장되어 있습니다.
fruits = ["apple", "banana", "cherry"]
# for문을 사용해 리스트의 각 요소를 순서대로 하나씩 꺼냅니다.
for fruit in fruits:
    # fruit 변수에 리스트의 각 값이 담겨 출력됩니다.
    print(f"과일 리스트를 이용한 for문 : {fruit}")

# 문자열을 활용한 for문 예제
print("\n문자열을 활용한 for문 예제 2")
# 문자열은 문자(character)들의 나열입니다.
# 문자열 word는 "Python"으로 초기화되어 있습니다.
word = "Python"
# for문을 사용해 문자열의 각 문자를 순서대로 하나씩 꺼냅니다.
for char in word:
    # char 변수에 문자열의 각 문자가 담겨 출력됩니다.
    print(f"문자열을 이용한 for문 : {char}")

# 튜플을 활용한 for문 예제
print("\n튜플을 활용한 for문 예제 3")
# 튜플: 변경 불가능한(immutable) 자료구조로, 여러 값을 묶어 저장할 수 있습니다.
# coordinates 리스트에는 튜플로 이루어진 좌표값이 저장되어 있습니다.
coordinates = [(1, 2), (3, 4), (5, 6)]
# for문에서 튜플의 각 요소를 꺼낼 때, 튜플을 두 변수(x, y)로 분해(unpacking)할 수 있습니다.
for x, y in coordinates:
    # 각 좌표의 x값과 y값이 출력됩니다.
    print(f"튜플을 이용한 for문 : {x}, {y} ")

# 딕셔너리를 활용한 for문 예제
print("\n딕셔너리를 활용한 for문 예제 4")
# 딕셔너리: key-value 쌍으로 데이터를 저장하는 자료구조입니다.
# person 딕셔너리에는 name, age, city 정보가 저장되어 있습니다.
person = {"name": "Python", "age": 25, "city": "Seoul"}
# 딕셔너리의 items() 메서드를 사용하면 key와 value를 동시에 가져올 수 있습니다.
for key, value in person.items():
    # key와 value 쌍을 출력합니다.
    print(f"딕셔너리를 활용한 for문 : key = {key}, value = {value}")

# range를 활용한 for문 예제
print("\nrange를 활용한 for문 예제 5")
# range(): 일정 범위의 숫자를 생성하는 함수입니다.
# range(1, 6)은 1부터 5까지의 숫자를 생성합니다.
for i in range(1, 6):
    # i 변수에 생성된 숫자가 하나씩 담겨 출력됩니다.
    print(f"range 범위 직접 지정 for문 : {i}")

# range(5)는 0부터 4까지의 숫자를 생성합니다.
for i in range(5):
    # i 변수에 생성된 숫자가 하나씩 담겨 출력됩니다.
    print(f"range 범위 마지막 지정 for문 : {i}")

# 집합(set)을 활용한 for문 예제
print("\n집합을 활용한 for문 예제 6")
# 집합(set): 중복을 허용하지 않고, 순서가 없는 데이터 구조입니다.
# unique_numbers 집합에는 중복되지 않는 정수 값들이 저장되어 있습니다.
unique_numbers = {1, 2, 3, 4, 5}
# for문으로 집합의 각 요소를 하나씩 꺼낼 수 있습니다.
for number in unique_numbers:
    # number 변수에 집합의 값이 하나씩 담겨 출력됩니다.
    # 집합은 순서가 없으므로 출력 순서는 일정하지 않습니다.
    print(f"집합을 활용한 for문 : {number}")

# 제너레이터를 활용한 for문 예제
print("\n제너레이터를 활용한 for문 예제 7")
# 제너레이터: 메모리를 효율적으로 사용할 수 있는 데이터 생성 방식입니다.
# 제너레이터 함수는 yield 키워드를 사용해 값을 하나씩 반환합니다.
def generator():
    # 0부터 2까지의 숫자를 생성합니다.
    for num in range(3):
        yield num  # yield를 통해 값을 반환하면서 함수 실행을 멈춥니다.

# for문으로 제너레이터 함수의 값을 하나씩 꺼낼 수 있습니다.
for value in generator():
    # value 변수에 제너레이터에서 반환된 값이 담겨 출력됩니다.
    print(f"제너레이터를 활용한 for문 : {value}")

# 리스트 슬라이싱(slicing)을 활용한 for문 예제
print("\n리스트 슬라이싱을 활용한 for문 예제 8")
# slices 리스트: 여러 개의 문자열을 포함하고 있는 리스트
slices = ["A", "B", "C", "D", "E"]

# 슬라이싱으로 리스트 전체 순회
# slices[0:5]는 리스트의 처음부터 끝까지 모든 요소를 가져옵니다.
for alphabet in slices[0:5]:
    print(f"전체 리스트 슬라이싱: {alphabet}")

print("\n리스트 처음부터 특정 범위까지 슬라이싱")
# slices[:3]는 인덱스 0부터 2까지의 요소를 가져옵니다. (인덱스 3은 포함되지 않음)
for alphabet in slices[:3]:
    print(f"처음부터 인덱스 2까지 슬라이싱: {alphabet}")

print("\n리스트 특정 인덱스부터 끝까지 슬라이싱")
# slices[3:]는 인덱스 3부터 끝까지의 요소를 가져옵니다.
for alphabet in slices[3:]:
    print(f"인덱스 3부터 끝까지 슬라이싱: {alphabet}")