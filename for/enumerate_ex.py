# enumerate 예제
print("enumerate example")

print("\n문자열을 이용한 enumerate 출력 예시")
str_data = "enumerate example"
for index, value in enumerate(str_data):
    print(index, "번: ", value)

print("\n리스트를 이용한 enumerate 출력 예시")
list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, value in enumerate(list_data):
    print(index, "번: ", value)