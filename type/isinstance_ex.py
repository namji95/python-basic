# isinstance 예제
print(f"isinstance 문자열 체크 예제")
data_str = "문자열 체크 테스트"
print(f"({data_str}) 데이터가 {type(data_str)}일 때 isinstance str로 설정 결과: {isinstance(data_str, str)}")
print(f"({data_str}) 데이터가 {type(data_str)}일 때 isinstance int로 설정 결과: {isinstance(data_str, int)}")

data_int = 123
print(f"\n({data_int}) 데이터가 {type(data_int)}일 때 isinstance str로 설정 결과: {isinstance(data_int, int)}")
print(f"({data_int}) 데이터가 {type(data_int)}일 때 isinstance int로 설정 결과: {isinstance(data_int, str)}")

data_list = [1, 2, 3]
print(f"\n({data_list}) 데이터가 {type(data_list)}일 때 isinstance list로 설정 결과: {isinstance(data_list, list)}")
print(f"({data_list}) 데이터가 {type(data_list)}일 때 isinstance str로 설정 결과: {isinstance(data_list, str)}")

data_dict = {"a": 1, "b": 2, "c": 3}
print(f"\n({data_dict}) 데이터가 {type(data_dict)}일 때 isinstance dict로 설정 결과: {isinstance(data_dict, dict)}")
print(f"({data_dict}) 데이터가 {type(data_dict)}일 때 isinstance str로 설정 결과: {isinstance(data_dict, str)}")