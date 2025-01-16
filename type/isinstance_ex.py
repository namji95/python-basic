# isinstance 예제
print(f"isinstance 문자열 체크 예제")
data_str = "문자열 체크 테스트"
print(f"({data_str}) 데이터가 {type(data_str)}일 때 isinstance str로 설정 결과: {isinstance(data_str, str)}")
print(f"({data_str}) 데이터가 {type(data_str)}일 때 isinstance int로 설정 결과: {isinstance(data_str, int)}")

print(f"\nisinstance 정수 체크 예제")
data_int = 123
print(f"({data_int}) 데이터가 {type(data_int)}일 때 isinstance str로 설정 결과: {isinstance(data_int, int)}")
print(f"({data_int}) 데이터가 {type(data_int)}일 때 isinstance int로 설정 결과: {isinstance(data_int, str)}")

print(f"\nisinstance 리스트 체크 예제")
data_list = [1, 2, 3]
print(f"({data_list}) 데이터가 {type(data_list)}일 때 isinstance list로 설정 결과: {isinstance(data_list, list)}")
print(f"({data_list}) 데이터가 {type(data_list)}일 때 isinstance str로 설정 결과: {isinstance(data_list, str)}")

print(f"\nisinstance 딕셔너리 체크 예제")
data_dict = {"a": 1, "b": 2, "c": 3}
print(f"({data_dict}) 데이터가 {type(data_dict)}일 때 isinstance dict로 설정 결과: {isinstance(data_dict, dict)}")
print(f"({data_dict}) 데이터가 {type(data_dict)}일 때 isinstance str로 설정 결과: {isinstance(data_dict, str)}")

print(f"\nisinstance 딕셔너리 안에 리스트인 데이터 체크 예제")
data_list_dict = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
print(f"({data_list_dict}) 데이터가 {type(data_list_dict)}일 때 isinstance dict로 설정 결과: {isinstance(data_list_dict, dict)}")
print(f"({data_list_dict}) 데이터가 {type(data_list_dict)}일 때 isinstance str로 설정 결과: {isinstance(data_list_dict, str)}")

print(f"\nisinstance 딕셔너리 안에 리스트인 데이터 체크 예제2")
for key, value in data_list_dict.items():
    print(f"({value}) 데이터가 {type(value)}일 때 isinstance list로 설정 결과: {isinstance(value, list)}")
    print(f"({value}) 데이터가 {type(value)}일 때 isinstance str로 설정 결과: {isinstance(value, str)}")