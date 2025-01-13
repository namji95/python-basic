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

print("\n딕셔너리를 이용한 enumerate 출력 예시")
dict_data = {
    "1": "A",
    "2": "B",
    "3": "C",
    "4": "D",
    "5": "E",
}
for index, (key, value) in enumerate(dict_data.items()):
    print(f"{index}번 - {key}: {value}")

print("\n딕셔너리에 리스트 데이터가 존재하는 경우의 데이터를 이용한 enumerate 출력 예시")
list_in_dict_data = {
    "1": "A",
    "2": ["B", "C"],
    "3": ["D", "E"],
}
for index, (key, value) in enumerate(list_in_dict_data.items()):
    print(f"{index}번 - {key}: {value}")

print("\n딕셔너리에 리스트 데이터가 존재하는 경우의 데이터를 이용한 enumerate 출력 예시2")
list_in_dict_data = {
    "1": ["A"],
    "2": ["B", "C", "D"],
    "3": ["E", "F"],
}
for index, (key, values) in enumerate(list_in_dict_data.items()):
    for idx, value in enumerate(values):
        print(f"{index}번의 - {key}: {values}의 {idx}번의 {value} 데이터")

print("\nenumerate 설정 변경")
new_dict_data = {
    "1": "A",
    "2": "B",
    "3": "C",
    "4": "D",
    "5": "E",
}
for index, (key, value) in enumerate(new_dict_data.items(), start=1):
    print(f"{index}번 - {key}: {value}")